from . import get_return_data
from . import correlation_test
from . import return_vs_nextReturn_plot

def main():
    print("***Starting Correlation Test***")
    get_return_data.main()
    correlation_test.main()
    print("***Correlation Test Complete***")
    return_vs_nextReturn_plot.main()
    

if __name__ == "__main__":
    main()