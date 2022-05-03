# Customer order prediction


<img src='data/cover.JPG' width=550></img>

## Problem statement

The purpose of this project is to present first steps towards designing a system that allows a per customer prediction if the customer makes a purchase in the horizon of the next 30 days.

The project is split into the following phases:
1. [EDA](src/01_EDA.ipynb) - initial analysis of data
1. [FEATURE ENGINEERING](src/02_FEATURE_ENGINEERING.ipynb) - formulating the target and feature variables
1. [MODELING](src/03_MODELING.ipynb) - modeling the target variable and evaluating results


## Project structure

```
├── data                                # Data used in the project
├── environment                         # Definition and contents of the project virtualenv
└── src                                 # Source files of the project
    └── utilities                       # Utility functions

```


## Resources
* Dataset: [customer order dataset](data/raw_data.csv)
* Working environment pre-requisites: Ubuntu18.04 LTS / Python 3.6.9 / virtualenv
* Use the `Makefile` commands to create (`create-env`) and activate (`activate-env-command`) the project virtual environment
