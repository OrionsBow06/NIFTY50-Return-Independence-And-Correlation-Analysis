import pandas as pd
import numpy as np 
from ..config import DATA, RESULT, LABEL

data_path = DATA
result_path = RESULT / "return_independence"

companies = pd.read_csv(data_path / "raw_data/ind_nifty50list.csv")
test_result = []
label = LABEL

def main():
    print("***Running Test***")
    for symbol in companies["Symbol"]:
        return_data = pd.read_csv(data_path / "derived_data/return_segregation_data"/ f"{symbol}_segregated_return_data.csv")
        test_process(symbol, return_data)
    print("***Test Complete***")

    df = pd.DataFrame(test_result)
    save_frame(df, "bin_test_result_raw.csv")
    df = process_data(df)
    print(df)
    save_frame(df, "bin_test_result_processed.csv")
    summary = prepare_summary(df)
    save_frame(summary, "bin_test_result_summary.csv")

def prepare_summary(df):
    summary = pd.DataFrame()
    summary["bin"] = label
    mean = []
    std = []
    for lab in label:
        mean.append(df[lab + " mean"].mean())   
        std.append(df[lab + " std"].mean())
    summary["expected mean"] = mean
    summary["expected std"] = std
    print(summary)
    return summary


def process_data(df):
    for lab in label:
        df.loc[df[lab + " std"] == 0, lab+ " mean"] = np.nan
        df.loc[df[lab + " std"] == 0, lab+ " std"] = np.nan
    return df

def save_frame(df, name):
    df.to_csv(result_path / name)

def test_process(symbol, return_data):
    mean_data = return_data[["Next Return", "bin"]].groupby(["bin"]).mean()
    std_data = return_data[["Next Return", "bin"]].groupby(["bin"]).std(ddof=0)
    data = {
            "Company Name": companies.loc[companies["Symbol"] == symbol]["Company Name"].values[0]
        }
    for lab in label:
        try:
            data[lab + " mean"] = mean_data.loc[lab].values[0]
            data[lab + " std"] = std_data.loc[lab].values[0]
        except KeyError:
            data[lab + " mean"] = np.nan
            data[lab + " std"] = np.nan
    test_result.append(data)

if __name__ == "__main__":
    main()

#     cor.append(np.corrcoef(return_data["Return"], return_data["Next Return"])[0,1])
#     return_mean.append(return_data["Return"].mean())
#     next_return_mean.append(return_data["Next Return"].mean())

# test_result["Expected Return"] = return_mean
# test_result["Expected Next Return"] = next_return_mean
# test_result["Correlation"] = cor
# test_result.to_csv(result_path+"corelational_test_result.csv")

# test_summary = pd.DataFrame()
# test_summary["Expected mean return (non weighted)"] = [test_result["Expected Return"].mean()]
# test_summary["Expected mean next return (non weighted)"] = [test_result["Expected Next Return"].mean()]
# test_summary["mean correlation"] = [test_result["Correlation"].mean()]
# test_summary.to_csv(result_path+"corelational_test_summary.csv")
