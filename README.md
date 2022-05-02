# Customer order prediction


<img src='data/cover.JPG' width=550></img>

Predicting placing an order in the horizon of the next 30 days


## Resources
* Dataset: [customer order dataset](data/raw_data.csv)
* Working environment pre-requisites: Ubuntu18.04 LTS / Python 3.6.9 / virtualenv
* Use the `Makefile` commands to:
  * `create-env` - create the project virtual environment

## Project structure

```
├── data                                # Data used in the project
├── environment                         # Definition and contents of the project virtualenv
└── src                                 # Source files of the project
    └── utilities                       # Utility functions

```

The analysis is split into the following phases:
1. [EDA](src/01_EDA.ipynb)
1. [FEATURE ENGINEERING](src/02_FEATURE_ENGINEERING.ipynb)
1. [MODELING](src/03_MODELING.ipynb)
