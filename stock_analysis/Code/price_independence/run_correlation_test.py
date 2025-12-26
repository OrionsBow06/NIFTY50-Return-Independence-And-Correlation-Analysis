from . import get_data
from . import correlation_test
from . import plot

def main():
    print("***Starting Correlation Test***")
    get_data.main()
    correlation_test.main()
    print("***Correlation Test Complete***")
    plot.main()

if __name__ == "__main__":
    main()