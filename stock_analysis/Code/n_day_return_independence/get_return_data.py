import pandas as pd
import numpy as np
from ..config import RAW, DERIVED
from pathlib import Path

global companies 
global data_path
global result_path


data_path = RAW
result_path = DERIVED
companies = pd.read_csv(data_path / "ind_nifty50list.csv")
num = 1

def main(n):
    global num
    num = n 
    print("***Fetching Data****")
    for symbol in companies["Symbol"]:
        get_return_data(symbol)
    print("***Process Complete***")

def get_return_data(symbol):   
    historical_data = pd.read_csv(data_path / "history_data" / f"{symbol}_history_data.csv")
    end_data = derive_return_data(historical_data)
    save_return_data(symbol, end_data)


def save_return_data(symbol, end_data):
    path = result_path / f"{num}_day_return_data"
    path.mkdir(exist_ok=True)
    return_data = pd.DataFrame(end_data[:-num])
    return_data.to_csv(path / f"{symbol}_{num}_day_return_data.csv")

def derive_return_data(historical_data):

    return_data = historical_data.copy()
    return_data["Return"] = (historical_data["Close"]-historical_data["Open"])/historical_data["Open"]
    return_data["Next Return"] = return_data["Return"].shift(-num)
    return return_data[["Date", "Open", "Close", "Return", "Next Return"]]

    # O(n^2) algorithm for deriving data
    # end_data = []
    # for date in historical_data["Date"]:
    #     row_data = historical_data.loc[historical_data["Date"] == date]
    #     if not(row_data["Open"].isna().any() or row_data["Close"].isna().any()):
    #         open_price = row_data["Open"].values[0]
    #         close_price = row_data["Close"].values[0]
    #         derived_data = {
    #                 "Date": date,
    #                 "Open": open_price,
    #                 "Close": close_price,
    #                 "Return": (close_price-open_price)/open_price,
    #                 "Next Return": -1
    #             }
    #         end_data.append(derived_data)
    # for i in range(len(end_data)-1):
    #     data = end_data[i]
    #     next_data = end_data[i+1]
    #     data["Next Return"] = next_data["Return"]
    # return end_data

   

if __name__ == "__main__":
    main(num)