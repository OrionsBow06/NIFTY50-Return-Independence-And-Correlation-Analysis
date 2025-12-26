import pandas as pd

def derive_return_data(historical_data):

    return_data = historical_data.copy()
    return_data["Return"] = (historical_data["Close"]-historical_data["Open"])/historical_data["Open"]
    return_data["Next Return"] = return_data["Return"].shift(-1)
    return return_data[["Date", "Open", "Close", "Return", "Next Return"]]

historical_data = pd.read_csv("D:/UofT/year 2/STA257/stock_analysis/Data/raw_data/history_data/COALINDIA_history_data.csv")
return_data = derive_return_data(historical_data)
# print (return_data.loc[return_data["Date"] == "2024-10-31 00:00:00+05:30"])
# print (return_data.loc[return_data["Date"] == "2024-11-01 00:00:00+05:30"])
# print (return_data.loc[return_data["Date"] == "2024-11-04 00:00:00+05:30"])
# print (return_data.loc[return_data["Date"] == "2024-11-05 00:00:00+05:30"])
# print (return_data.loc[return_data["Date"] == "2024-11-06 00:00:00+05:30"])
# print (return_data.loc[return_data["Date"] == "2024-11-07 00:00:00+05:30"])