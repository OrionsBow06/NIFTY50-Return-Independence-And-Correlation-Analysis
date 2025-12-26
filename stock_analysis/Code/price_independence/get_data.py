import yfinance as yf
import pandas as pd
from ..config import RAW

def main():
    print("***Fetching Data***")
    path = RAW
    companies = pd.read_csv(path / "ind_nifty50list.csv")
    symbols = companies["Symbol"]
    for symbol in symbols:
        company = yf.Ticker(symbol+".BO")
        data = company.history(period = "5y").dropna()
        data.to_csv(path / "history_data" / f"{symbol}_history_data.csv")
    print("***Process completed***")

if __name__ == "__main__":
    main()