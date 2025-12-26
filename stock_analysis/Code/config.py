from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CODE = ROOT / "Code"
DATA = ROOT / "DATA"
DERIVED = DATA / "derived_data"
RAW = DATA / "raw_data"
RESULT = ROOT / "RESULT"

LABEL = ["inf", "(-0.2,-0.15)", "(-0.15,-0.1)", "(-0.1,-0.05)", "(-0.05,0.0)",
        "(0.0,0.05)", "(0.05,0.1)", "(0.1,0.15)", "(0.15,0.2)", "sup"]

BIN =  [-50,-0.2, -0.15, -0.1, -0.05, 0.0, 0.05, 0.1, 0.15, 0.2,50]

DAYS = [1, 5, 10, 15, 20, 25, 30]

COLOUR = ["Blue", "Orange", "Green", "Red", "Brown", "Purple", "Pink", "Grey", "Black", "Cyan"]
