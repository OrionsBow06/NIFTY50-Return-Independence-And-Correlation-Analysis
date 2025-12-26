import pandas as pd
import numpy as np 
from ..config import DATA, RESULT

data_path = DATA
result_path = RESULT / "n_day_return_independence"
cor = []
return_mean = []
next_return_mean = []
companies = pd.read_csv(data_path / "raw_data/ind_nifty50list.csv")
num = 1

def main(n): 
    set_param(n)
    print("***Running Test***")
    for symbol in companies["Symbol"]:
        compute_return_data(symbol)
    print("***Test Complete***")

    test_result = prepare_and_save_result()
    print(test_result)
    prepare_and_save_summary(test_result)

def set_param(n):
    cor.clear()
    return_mean.clear()
    next_return_mean.clear()
    global num 
    num = n

def prepare_and_save_summary(test_result):
    test_summary = pd.DataFrame()
    test_summary["Expected return"] = [test_result["Expected Return"].mean()]
    test_summary["Expected next return"] = [test_result["Expected Next Return"].mean()]
    test_summary["Expected correlation"] = [test_result["Correlation"].mean()]
    test_summary.to_csv(result_path / f"{num}_day_corelational_test_summary.csv")
    print(test_summary)

def prepare_and_save_result():
    result_path.mkdir(exist_ok= True)
    test_result = pd.DataFrame()
    test_result["Company Name"] = companies["Company Name"]
    test_result["Expected Return"] = return_mean
    test_result["Expected Next Return"] = next_return_mean
    test_result["Correlation"] = cor
    test_result.to_csv(result_path / f"{num}_day_corelational_test_result.csv")
    return test_result

def compute_return_data(symbol):
    return_data = pd.read_csv(data_path / f"derived_data/{num}_day_return_data" / f"{symbol}_{num}_day_return_data.csv")
    cor.append(np.corrcoef(return_data["Return"], return_data["Next Return"])[0,1])
    return_mean.append(return_data["Return"].mean())
    next_return_mean.append(return_data["Next Return"].mean())

if __name__ == "__main__":
    main(num)