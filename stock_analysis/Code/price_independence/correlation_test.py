from . import computation
import pandas as pd
import numpy as np
from ..config import RAW, RESULT

data_path = RAW
result_path = RESULT / "price_independence"

companies = pd.read_csv(data_path / "ind_nifty50list.csv")
symbols = companies["Symbol"]
open_mean = []
open_std = []
close_mean = []
close_std = []
cor = []
result_data = []

def main():
    print("*** Running Test ***")
    for symbol in symbols:
        compute_correlation_data(symbol) 
    result_summary_data = prepare_summary_data()
    result_data_df = pd.DataFrame(result_data)
    save_and_print(result_data_df, "correlation_test_result.csv")
    result_summary_df = pd.DataFrame(result_summary_data)
    save_and_print(result_summary_df, "Correlation_test_summary.csv")
    print("*** Test Completed ***")


def save_and_print(data_df, name):
    data_df.to_csv(result_path / name )
    print(data_df)

def prepare_summary_data():
    return [{
        "Expected open: ": np.array(open_mean).mean(),
        "Expected open std: ": np.array(open_std).mean(),
        "Expected close: ": np.array(close_mean).mean(),
        "Expected close std: ": np.array(close_std).mean(),
        "Expected correlation: ": np.array(cor).mean(),
    }]

def compute_correlation_data(symbol):
    open_data = computation.compute_open_data(symbol)
    close_data = computation.compute_close_data(symbol)
    correlation = computation.compute_open_close_relation(symbol)
    result_data.append({
            "Company Name": companies.loc[companies["Symbol"] == symbol]["Company Name"],
            "Open Mean: ": open_data[0],
            "Open Variance: ": open_data[1],
            "Open std: ": open_data[2],
            "Close Mean: ": close_data[0],
            "Close Variance: ": close_data[1],
            "Close std: ": close_data[2],
            "Covarience: ": correlation[0],
            "Correlation: ": correlation[1]
        })
    open_mean.append(open_data[0])
    open_std.append(open_data[2])
    close_mean.append(close_data[0])
    close_std.append(close_data[2])
    cor.append(correlation[1])

if __name__ == "__main__":
    main()