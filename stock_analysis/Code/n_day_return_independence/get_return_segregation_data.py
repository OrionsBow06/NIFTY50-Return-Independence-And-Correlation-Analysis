import pandas as pd 
import pandas as pd
import numpy as np
from ..config import DATA, LABEL, BIN



data_path = DATA
result_path = DATA / "derived_data"
companies = pd.read_csv(data_path / "raw_data/ind_nifty50list.csv")
num = 1
def main(n):
    global num
    num = n
    print("***Fetching Data****")
    for symbol in companies["Symbol"]:
        get_return_data(symbol)
    print("***Process Complete***")

def get_return_data(symbol):
    return_data = pd.read_csv(data_path / f"derived_data/{num}_day_return_data" / f"{symbol}_{num}_day_return_data.csv")
    end_data = segregate_return_data(return_data)
    save_return_data(symbol, end_data)

def save_return_data(symbol, end_data):

    path = result_path / f"{num}_day_return_segregation_data"
    path.mkdir(exist_ok=True)
    end_data.to_csv(path / f"{symbol}_segregated_{num}_day_return_data.csv")

def segregate_return_data(return_data):
    rd = return_data.copy()
    bin = BIN
    label = LABEL
    rd["bin"] = pd.cut(return_data["Return"], bins = bin, labels = label)
    return rd[["Date", "Open", "Close", "Return", "Next Return", "bin"]]

if __name__ == "__main__":
    main(num)