# NIFTY50-Return-Independence-And-Correlation-Analysis

## Description

The project aims to study the **temporal relation of returns and stock prices** by considering the Indian equity market and using the historical **NIFTY50** data. 

The study tries to answer the following questions: 

1) Are the open prices and the close prices of a day independent? If not, what is their relation?
2) Are today's return and tomorrow's return independent? If not, what is their relation ?
3) Are today's return and return after $n$ days independent? If not, what is their relation?

As per the study, brief answers to the stated questions is as follows:

1) for a single day, the open prices and close prices and very closely related and have a linear relationship.
2) today's and tomorrow's return have negligible linear correlation ($|E[cor]|<0.008$). However, conditioning on large absolute returns today, point towards increased variability the next day, which is consistent with volatility clustering.
3) today's return and return after $n$ days also exhibit near 0 linear correlation($|E[cor]|<0.006$). Conditional analysis suggests the expected future returns remain close to 0, with the dispersion of returns increasing with $n$. 

The interested individual to understand only the general, technical, and coding aspects of the project may only read the README. For a more detailed summary, interpretation and understanding, may refer to *stock_analysis/detailed_project_summary.pdf*.

For info regarding the contents of the detailed summary, refer to the **Detailed Summary Info** section of the README

## Motivation 

An essential assumption in financial modeling is to assume daily return to be approximately independent and identically distributed i.e. daily returns are treated as i.i.d random variables across time. Based on this, they can be studied using the theory of stochastic processes. This project tests this assumption by directly using real market data. 

Hence the aim of the project shifts from trying to predict the market or search for an $/alpha$, but to understanding 

- the structure of the market
- the relationship of prices and returns
- the distribution of market data (both derived and raw)
- behaviour of time v/s return, beyond linear correlation

## Data

**Universe**: *NIFTY50 constituent stocks*
**Frequency**: *Daily Data*
**Period**: Last ~5 years (2021-2025 inclusive)
**Source**: Publicaly available historical price data

### Data Collection details
- The official list of NIFTY50 constituents (ind_nifty50list) was obtained from "niftyindices.com" 
- Historical price data was fetched using the "yfinance" API (Yahoo Finance)
- Data was stored and processed using "pandas" and saved as CSV files

## Directory Structure

## Project Structure (key files)

```text
D:.
│   README.md
│
└── stock_analysis
    │   README.md
    │   run_project.py                      # to run the whole project from scratch
    │   __init__.py
    │
    ├── Data                                # holds all data (raw and derived) except for results
    │   ├── derived_data                    # contains all derived data
    │   │   ├── return_data                 # one day return data
    │   │   └── return_segregation_data    # segregated one day return data for bin test
    │   └── raw_data                        # raw data
    │       ├── ind_nifty50list.csv         # constituent list
    │       └── history_data                # historical price data
    │
    ├── Code                                # holds all code and tests for the project
    │   │   config.py
    │   │   __init__.py
    │   ├── price_independence              # tests related to prices
    │   │   │   correlation_test.py
    │   │   │   get_data.py
    │   │   │   plot.py
    │   │   │   run_correlation_test.py     # runner for complete correlation test pipeline
    │   │   │   __init__.py
    │   │
    │   ├── return_independence             # tests related to daily return 
    │   │   │   correlation_test.py
    │   │   │   get_return_data.py
    │   │   │   get_return_segregation_data.py
    │   │   │   bin_test.py
    │   │   │   return_vs_nextReturn_plot.py
    │   │   │   bin_test_plot.py
    │   │   │   run_correlation_test.py
    │   │   │   run_bin_test.py
    │   │   │   __init__.py
    │   │
    │   └── n_day_return_independence       # tests related to n day returns
    │       │   __init__.py
    │       │   n_day_bin_test_plot.py
    │       │   bin_test.py
    │       │   correlation_test.py
    │       │   get_return_data.py
    │       │   get_return_segregation_data.py
    │       │   return_vs_nextReturn_plot.py
    │       │   rough.py
    │       │   run_bin_test.py
    │       │   run_correlation_test.py
    │       │   correlation_test_summary.py
    │       │   bin_test_summary.py
    │       │   all_day_bin_test_plot.py
    │       │   correlation_test_plot.py    
    │       └── abs_correlation_test_plot.py
    │
    └── result                              # holds results and plots for tests in Code
        ├── price_independence
        │       Correlation_test_summary.csv
        │       correlation_test_result.csv
        │       open_vs_close.jpeg
        │
        ├── return_independence
        │       Return_VS_Next_Return.jpeg
        │       corelational_test_result.csv
        │       corelational_test_summary.csv
        │       bin_test_result_raw.csv
        │       bin_test_result_summary.csv
        │       bin_test_result_processed.csv
        │       Segregated_Return_VS_Expected_Next_Return.jpeg
        │
        └── n_day_return_independence
                Segregated_Return_VS_Expected_Next_30_Return.jpeg
                Return_VS_Next_1_Return.jpeg
                Return_VS_Next_5_Return.jpeg
                Return_VS_Next_10_Return.jpeg
                Return_VS_Next_15_Return.jpeg
                Return_VS_Next_20_Return.jpeg
                Return_VS_Next_25_Return.jpeg
                Return_VS_Next_30_Return.jpeg
                bin_test_summary.csv
                Day_VS_Correlation.jpeg
                Day_VS_abs_Correlation.jpeg
                corelation_test_summary.csv
```
    
## Design Choices

While designing the project, best efforts have been made to keep the project modular. Major design choices include:

- **Concern clasification**: The whole project is sepearated in Data, Code and Result. This provides modularity to the project and keeps the different layers in the study (resources -> test -> result) seperated. 
- **Objective based code organisation**: Inside code, the scripts are classified with respect to the objective that they are related to. Each folder is treated as its own package making imports easier, testing cleaner and code scalable. 
- **Centeral config file**: The centeral config file inside Code defined global paths and global constants making it easier to debug and safer to refactor.
- **Runner pipelines**: There are runner pipelines for the project as a whole and for each test in the study. These act as single entry points for whole processes, making the action of running a complete analysis easier, faster and more accessible.
- **Result mirrors Code**: The file structure inside result mirrors the structure inside Code. This makes it easy to trace the output of code

## Dependencies 

### Code Dependencies
for code dependencies, please refer to requirment.txt

### Data Dependencies 
List of NIFTY50 constituents: *stock_analysis/Data/raw_data/ind_nifty50list.csv*
Historical Price data of NIFTY50constituents: *stock_analysis/Data/raw_data/history_data*

## How to run
It is advised that the "non-technical" user limits to running pipelines. The pipelines are supposed to be run from the terminal. I list the pipelines along with their run commands. The run commands are to be run from the root address i.e. "..../stock_analysis"

- **Project pipeline** :

    ```py -m run_project```
- **Correlation test (price_independence)** :

    ``` py -m Code.price_independence.run_correlation_test```
- **Correlation test (return_independence)**:

    ``` py -m Code.return_independence.run_correlation_test```
- **bin test (return_independence)**:

    ``` py -m Code.return_independence.run_bin_test ```
- **Correlation test (n_day_return_independence)**:

    ``` py -m Code.n_day_return_independence.run_correlation_test```
- **bin test (n_day_return_independence)**: 

    ```py -m Code.n_day_return_independence.run_bin_test```

## Detailed Summary Info

A detailed summary of the project is documented in *stock_analysis/detailed_project_summary.pdf*. It elaborates on:

- **Project setup and assumptions**
- **Methodology used**
- **Key findings**
- **Interpretation and limitations of the analysis**

The summary emphasizes the **academic aspects** of the study, focusing on rigorous exploration and understanding of market behavior and temporal dependencies of returns, rather than purely technical implementation details.


## Author

**Karan Chauhan** - University of Toronto
karan.chauhann2006@gmail.com / karan.chauhan@mail.utoronto.ca



## Future Works

This project can be extended in several directions:

1) Studying other markets such as the S&P500, or extending the dataset from 5 years to 10 years or even the full historical period available.
2) Investigating return behavior over longer horizons to better understand temporal dependencies.
3) Analyzing specific anomalies or peculiar patterns in the data to uncover deeper insights into market structure.

