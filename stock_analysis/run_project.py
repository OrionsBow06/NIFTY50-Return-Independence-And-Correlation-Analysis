from Code.price_independence import run_correlation_test as pirc
from Code.return_independence import run_correlation_test as rirc, run_bin_test as rirb
from Code.n_day_return_independence import run_correlation_test as nrirc, run_bin_test as nrirb

def main():
    print("Starting project")
    price_independence()
    return_independence()
    n_day_return_independence()
    print("project completed succesfully")

def price_independence():
    print("* OBJECTIVE: PRICE INDEPENDENCE *")
    pirc.main()
    print("*PRICE INDEPENDENCE COMPLETE*")

def return_independence():
    print("* OBJECTIVE: RETURN INDEPENDENCE *")
    rirc.main()
    rirb.main()
    print("*RETURN INDEPENDENCE COMPLETE*")

def n_day_return_independence():
    print("* OBJECTIVE: N DAY RETURN INDEPENDENCE *")
    nrirc.main()
    nrirb.main()
    print("*N DAY RETRUN INDEPENDENCE COMPLETE*")

if __name__ == "__main__":
    main()