import matplotlib.pyplot as plt
import pandas as pd 
from ..config import RESULT, LABEL, DAYS, COLOUR

data_path = RESULT / "n_day_return_independence"
result_path = RESULT / "n_day_return_independence"

def main():
    print("Plottting Data")
    fig, ax = plt.subplots(figsize = (12,6))
    plot_data(ax)
    set_properties(ax)
    fig.savefig(result_path / f"Segregated_Return_VS_Expected_Next_Return.jpeg")
    print("Plot saved")

def set_properties(ax):
    ax.set_xlabel("Return bin on date d")
    ax.set_ylabel(f"expected Return on date d+n")
    ax.set_title(f"segregated Return on d v/s expected Return on d+n")

def plot_data(ax):
    data = pd.read_csv(data_path / "bin_test_summary.csv")
    label = LABEL
    for i in range(len(DAYS)) :
        ax.errorbar(label, data[f"{DAYS[i]} expected mean"], 
                    yerr = data[f"{DAYS[i]} expected std"], ecolor=COLOUR[i])

if __name__ == "__main__":
    main()