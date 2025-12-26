import matplotlib.pyplot as plt 
import pandas as pd 
from Code.config import DATA, RESULT

data_path = DATA
result_path = RESULT / "return_independence/"
companies = pd.read_csv(data_path / "raw_data/ind_nifty50list.csv")

def main(): 
    fig, ax = plt.subplots()
    plot_data(ax)
    set_properties(ax)
    plt.show()
    fig.savefig(result_path / "Return_VS_Next_Return.jpeg")

def set_properties(ax):
    ax.set_xlabel("Return on date d")
    ax.set_ylabel("Return on date d+1")
    ax.set_title("Return on d v/s Return on d+1")

def plot_data(ax):
    for symbol in companies["Symbol"]:
        data = pd.read_csv(data_path / "derived_data/return_data" / f"{symbol}_return_data.csv")
        ax.scatter(data["Return"], data["Next Return"], color = "blue")
    
if __name__ == "__main__":
    main()