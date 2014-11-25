from copy import deepcopy
import random
from model.individual import Route, Individual
from utils.config import Config


class Operators(object):
    def __init__(self, settings=Config()):
        self._settings = settings

    @property
    def settings(self):
        return self._settings

    def _generate_individual(self):
        depots = self.settings.depots
        random.shuffle(depots)
        result = Individual()
        for depot in depots:
            result.add_depot(depot, self.settings.max_capacity)
        return result

    def _generate_individual2(self):
        depots = list(self.settings.depots)
        random.shuffle(depots)
        result = Individual()
        i = 0
        while depots:
            k = random.randrange(1, len(depots) + 1)
            result.routes.append(Route(i, depots[0:k]))
            del depots[0:k]
            i += 1
        return result

    def init_population(self, size=100):
        population = []
        for i in range(size):
            population.append(self._generate_individual())
        return population

    def init_population2(self, size=100):
        population = []
        for i in range(size):
            population.append(self._generate_individual2())
        return population

    def evaluate_individual(self, individual):
        distance_matrix = self.settings.distance_matrix
        total_distance = 0
        for route in individual.routes:
            total_distance += route.calculate_length(distance_matrix)
        return total_distance

    @staticmethod
    def _get_random_subroute(individual):
        random_route = random.choice(individual.routes).depots
        random_route_len = len(random_route)
        if random_route_len <= 1:
            return random_route
        start_idx = random.randrange(0, random_route_len - 1)
        end_idx = random.randrange(start_idx + 1, random_route_len + 1)
        return random_route[start_idx:end_idx]

    def _insert_subroute(self, subroute, individual):
        distances = self.settings.distance_matrix
        first_depot_of_subroute = subroute[0]
        closest_depot_no = first_depot_of_subroute.get_closest_depot_no(distances)
        for route_idx in xrange(len(individual.routes)):
            current_route = individual.routes[route_idx]
            if current_route.contains_depot(closest_depot_no):
                current_route.insert_subroute(subroute, after=closest_depot_no)

    def crossover(self, first_individual, second_individual):
        descendant = Individual.of(first_individual)
        subroute = self._get_random_subroute(second_individual)
        self._insert_subroute(subroute, descendant)
        descendant.normalize(self.settings.max_capacity)
        return descendant

    def swap(self, individual):
        routes = individual.routes
        first_route_idx = random.randrange(0, len(routes))
        first_dept_idx = random.randrange(0, len(routes[first_route_idx].depots))

        second_route_idx = random.randrange(0, len(routes))
        second_dept_idx = random.randrange(0, len(routes[second_route_idx].depots))

        first = routes[first_route_idx].depots[first_dept_idx]
        routes[first_route_idx].depots[first_dept_idx] = routes[second_route_idx].depots[
            second_dept_idx]
        routes[second_route_idx].depots[second_dept_idx] = first
        individual.normalize(self.settings.max_capacity)





