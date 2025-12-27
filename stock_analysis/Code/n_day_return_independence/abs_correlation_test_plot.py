import matplotlib.pyplot as plt
import pandas as pd 
from ..config import RESULT, LABEL, DAYS, COLOUR

data_path = RESULT / "n_day_return_independence"
result_path = RESULT / "n_day_return_independence"

def main():
    print("Plottting Data")
    
    plot_data()
    set_properties()
    plt.savefig(result_path / f"Day_VS_abs_Correlation.jpeg")
    print("Plot saved")

def set_properties():
    plt.xlabel("# days after date d")
    plt.ylabel(f"expected Correlation")
    plt.title(f"# days after d v/s expected abs correlation")

def plot_data():
    data = pd.read_csv(data_path / "corelation_test_summary.csv")
    plt.plot(data["Day"], abs(data["Expected correlation"]))

if __name__ == "__main__":
    main()