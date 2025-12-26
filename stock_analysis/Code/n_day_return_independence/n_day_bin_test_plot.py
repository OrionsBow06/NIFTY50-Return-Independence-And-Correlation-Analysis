import matplotlib.pyplot as plt
import pandas as pd 
from ..config import RESULT, LABEL

data_path = RESULT / "n_day_return_independence"
result_path = RESULT / "n_day_return_independence"
num = 1

def main(n):
    global num
    num = n
    print("Plottting Data")
    fig, ax = plt.subplots(figsize = (12,6))
    plot_data(ax)
    set_properties(ax)
    fig.savefig(result_path / f"Segregated_Return_VS_Expected_Next_{num}_Return.jpeg")
    print("Plot saved")

def set_properties(ax):
    ax.set_xlabel("Return bin on date d")
    ax.set_ylabel(f"expected Return on date d+{num}")
    ax.set_title(f"segregated Return on d v/s expected Return on d+{num}")

def plot_data(ax):
    data = pd.read_csv(data_path / f"{num}_day_bin_test_result_summary.csv")
    label = LABEL
    ax.errorbar(label, data["expected mean"], yerr = data["expected std"], ecolor= "blue")

if __name__ == "__main__":
    main(num)