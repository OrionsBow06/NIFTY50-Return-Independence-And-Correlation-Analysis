import matplotlib.pyplot as plt
import pandas as pd 
from ..config import RESULT, LABEL

data_path = RESULT / "return_independence"
result_path = RESULT / "return_independence"


def main():
    fig, ax = plt.subplots(figsize = (12,6))

    plot_data(ax)

    set_properties(ax)
    plt.show()
    fig.savefig(result_path / "Segregated_Return_VS_Expected_Next_Return.jpeg")

def set_properties(ax):
    ax.set_xlabel("Return bin on date d")
    ax.set_ylabel("expected Return on date d+1")
    ax.set_title("segregated Return on d v/s expected Return on d+1")

def plot_data(ax):
    data = pd.read_csv(data_path / "bin_test_result_summary.csv")
    label = LABEL
    ax.errorbar(label, data["expected mean"], yerr = data["expected std"], ecolor= "blue")

if __name__ == "__main__":
    main()