import matplotlib.pyplot as plt 
import pandas as pd 
from Code.config import DATA, RESULT

data_path = DATA
result_path = RESULT / "n_day_return_independence"
companies = pd.read_csv(data_path / "raw_data/ind_nifty50list.csv")
num = 1 

def main(n): 
    global num
    num = n
    print("Plottting Data")
    fig, ax = plt.subplots()
    plot_data(ax)
    set_properties(ax)
    fig.savefig(result_path / f"Return_VS_Next_{num}_Return.jpeg")
    print("Plot saved")

def set_properties(ax):
    ax.set_xlabel("Return on date d")
    ax.set_ylabel(f"Return on date d+{num}")
    ax.set_title(f"Return on d v/s Return on d+{num}")

def plot_data(ax):
    result_path.mkdir(exist_ok= True)
    for symbol in companies["Symbol"]:
        data = pd.read_csv(data_path / f"derived_data/{num}_day_return_data" / f"{symbol}_{num}_day_return_data.csv")
        ax.scatter(data["Return"], data["Next Return"], color = "blue")
    
if __name__ == "__main__":
    main(num)