import pandas as pd
from ..config import DAYS, RESULT, LABEL

data_path = RESULT / "n_day_return_independence"
result_path = RESULT / "n_day_return_independence"

def main():
    summary = pd.DataFrame()
    prepare_summary(summary)
    save_summary(summary)
    print("bin test summary saved")

def save_summary(summary_lst):
    summary = pd.DataFrame(summary_lst)
    summary.to_csv(result_path / "bin_test_summary.csv")

def prepare_summary(summary):
    summary["bin"] = LABEL
    for day in DAYS:
        day_data = pd.read_csv(data_path / f"{day}_day_bin_test_result_summary.csv")
        summary[f"{day} expected mean"] = day_data["expected mean"]
        summary[f"{day} expected std"] = day_data["expected std"]

    
        
if __name__ == "__main__":
    main()