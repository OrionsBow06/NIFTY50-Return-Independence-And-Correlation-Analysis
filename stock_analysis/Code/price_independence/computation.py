import numpy as np
import pandas as df
from ..config import RAW

path = RAW

def compute_open_data(symbol: str) -> list:
    data = df.read_csv(path / "history_data" / f"{symbol}_history_data.csv").dropna(subset= ["Open", "Close"])
    open_data = data["Open"]
    return [open_data.mean(), open_data.var(), open_data.std()]
    
def compute_close_data(symbol: str) -> list:
    data = df.read_csv(path / "history_data" / f"{symbol}_history_data.csv").dropna(subset= ["Open", "Close"])
    close_data = data["Close"]
    return [close_data.mean(), close_data.var(), close_data.std()]
    
def compute_open_close_relation(symbol: str) -> list:
    data = df.read_csv(path / "history_data" / f"{symbol}_history_data.csv").dropna(subset= ["Open", "Close"])
    open_data = data["Open"]
    close_data = data["Close"]
    return [np.cov(open_data, close_data)[0,1], np.corrcoef(open_data, close_data)[0,1]]
        
    
    



