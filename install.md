# Genetic_Algorithm_vehicle_routing guide installation

## Prerequisites

- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html)
- Optional [Mamba](https://mamba.readthedocs.io/en/latest/)

## Create environment

```bash
conda env create --file environment.yml --name genetic_algorithm_vehicle_routing
conda activate genetic_algorithm_vehicle_routing
```

or 

```bash
mamba env create -f environment.yml
activate genetic_algorithm_vehicle_routing
```

The packages necessary to run the project are now installed inside the conda environment.

**Note: The following sections assume you are located in your conda environment.**

## Set up project's module

To move beyond notebook prototyping, all reusable code should go into the `genetic_algorithm_vehicle_routing/` folder package. To use that package inside your project, install the project's module in editable mode, so you can edit files in the `genetic_algorithm_vehicle_routing` folder and use the modules inside your notebooks :

```bash
pip install --editable .
```

To use the module inside your notebooks, add `%autoreload` at the top of your notebook :

```python
%load_ext autoreload
%autoreload 2
```

Example of module usage :

```python
from genetic_algorithm_vehicle_routing.utils.paths import data_dir
data_dir()
```

## Set up Git diff for notebooks and lab

We use [nbdime](https://nbdime.readthedocs.io/en/stable/index.html) for diffing and merging Jupyter notebooks.

To configure it to this git project :

```
nbdime config-git --enable
```

To enable notebook extension :

```
nbdime extensions --enable --sys-prefix
```

Or, if you prefer full control, you can run the individual steps:

```
jupyter serverextension enable --py nbdime --sys-prefix

jupyter nbextension install --py nbdime --sys-prefix
jupyter nbextension enable --py nbdime --sys-prefix

jupyter labextension install nbdime-jupyterlab
```

You may need to rebuild the extension : `jupyter lab build`

## Set up Plotly for Jupyterlab

Plotly works in notebook but further steps are needed for it to work in Jupyterlab :

* @jupyter-widgets/jupyterlab-manager # Jupyter widgets support
* plotlywidget  # FigureWidget support
* @jupyterlab/plotly-extension  # offline iplot support

There are conflict versions between those extensions so check the [latest Plotly README](https://github.com/plotly/plotly.py#installation-of-plotlypy-version-3) to ensure you fetch the correct ones. 

```
jupyter labextension install @jupyter-widgets/jupyterlab-manager@0.36 --no-build
jupyter labextension install plotlywidget@0.2.1  --no-build
jupyter labextension install @jupyterlab/plotly-extension@0.16  --no-build
jupyter lab build
```
