from unittest import TestCase
from model.depot import Depot
from model.individual import Route, Individual

__author__ = 'Marek'


class TestRoute(TestCase):
    def setUp(self):
        self.distance_matrix = [
            [0, 1, 9, 4, 2, 7, 10, 3, 8, 5],
            [1, 0, 7, 9, 6, 6, 10, 8, 8, 5],
            [9, 7, 0, 9, 7, 5, 1, 1, 4, 5],
            [4, 9, 9, 0, 1, 3, 2, 6, 8, 1],
            [2, 6, 7, 1, 0, 6, 4, 6, 1, 1],
            [7, 6, 5, 3, 6, 0, 7, 5, 1, 8],
            [10, 10, 1, 2, 4, 7, 0, 10, 6, 2],
            [3, 8, 1, 6, 6, 5, 10, 0, 5, 4],
            [8, 8, 4, 8, 1, 1, 6, 5, 0, 6],
            [5, 5, 5, 1, 1, 8, 2, 4, 6, 0]
        ]
        self.depots = [
            Depot(1, 34),
            Depot(2, 45),
            Depot(3, 50),
            Depot(4, 34),
            Depot(5, 21),
            Depot(6, 67),
            Depot(7, 34),
            Depot(8, 56),
            Depot(9, 85)
        ]

    def test_calculate_length_one_depot(self):
        depots = self.depots[0:1]
        route = Route(0, depots)
        length = route.calculate_length(self.distance_matrix)
        self.assertTrue(length == 2)

    def test_calculate_length_many_depots(self):
        depots = self.depots[0:3]
        route = Route(0, depots)
        length = route.calculate_length(self.distance_matrix)
        self.assertEqual(length, 21)

    def test_normalize(self):
        individual = Individual([Route(0, self.depots)])
        individual.normalize(100)

        self.assertGreater(len(individual.routes), 1)
        for route in individual.routes:
            self.assertTrue(route.sum_of_demands() <= 100)

        depots_in_individual = [depot for route in individual.routes for depot in route.depots]
        self.assertItemsEqual(depots_in_individual, self.depots)
