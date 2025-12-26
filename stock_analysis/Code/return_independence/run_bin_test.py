from . import get_return_segregation_data
from . import bin_test
from . import bin_test_plot

def main():
    print("*** Starting Bin Test***")
    get_return_segregation_data.main()
    bin_test.main()
    print("***Completed Bin Test***")
    bin_test_plot.main()

if __name__ == "__main__":
    main()