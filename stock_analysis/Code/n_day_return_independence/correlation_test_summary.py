import pandas as pd
from ..config import DAYS, RESULT

data_path = RESULT / "n_day_return_independence"
result_path = RESULT / "n_day_return_independence"

def main():
    summary_lst = prepare_summary()
    save_summary(summary_lst)
    print("corelation test summary saved")

def save_summary(summary_lst):
    summary = pd.DataFrame(summary_lst)
    summary.to_csv(result_path / "corelation_test_summary.csv")

def prepare_summary():
    summary_lst = []
    for day in DAYS:
        day_data = pd.read_csv(data_path / f"{day}_day_corelational_test_summary.csv")
        data = {
            "Day" : day,
            "Expected return": day_data["Expected return"].values[0],
            "Expected next return" : day_data["Expected next return"].values[0],
            "Expected correlation": day_data["Expected correlation"].values[0]
        }
        summary_lst.append(data)
    return summary_lst
        
if __name__ == "__main__":
    main()