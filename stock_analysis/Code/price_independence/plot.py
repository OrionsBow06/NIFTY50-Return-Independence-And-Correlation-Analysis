import matplotlib.pyplot as mp
import pandas as pd
from ..config import RAW, RESULT

data_path = RAW
result_path = RESULT / "price_independence"
companies = pd.read_csv(data_path / "ind_nifty50list.csv")

def main():

    fig, ax = mp.subplots() 
    plot_data(ax)
    set_properties(ax)
    mp.show()
    fig.savefig(result_path / "open_vs_close.jpeg")

def set_properties(ax):
    ax.set_xlabel("Open Price")
    ax.set_ylabel("Close Price")
    ax.set_title("Open Price V/S Close Price")

def plot_data(ax):
    for symbol in companies["Symbol"]:
        data = pd.read_csv(data_path / "history_data"/ f"{symbol}_history_data.csv")
        ax.scatter(data["Open"], data["Close"], color = "blue")

if __name__ == "__main__":
    main()