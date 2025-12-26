from . import get_return_segregation_data
from . import bin_test
from . import n_day_bin_test_plot
from . import bin_test_summary
from ..config import DAYS

def main():
    print("*** Starting Bin Test***")
    for num in DAYS:
        get_return_segregation_data.main(num)
        bin_test.main(num)
        n_day_bin_test_plot.main(num)
    bin_test_summary.main()
    print("***Completed Bin Test***")

if __name__ == "__main__":
    main()