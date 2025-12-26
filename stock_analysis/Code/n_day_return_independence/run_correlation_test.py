from . import get_return_data
from . import correlation_test
from . import return_vs_nextReturn_plot
from . import correlation_test_summary
from ..config import DAYS

def main():
    print("***Starting Correlation Test***")
    for num in DAYS:
        get_return_data.main(num)
        correlation_test.main(num)
        return_vs_nextReturn_plot.main(num)
    correlation_test_summary.main()
    print("***Correlation Test Complete***")
    

if __name__ == "__main__":
    main()