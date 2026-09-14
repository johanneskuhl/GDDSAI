import csv

import os

import pandas

if os.path.isfile("data/runs.csv"):
    with open("data/runs.csv", "r") as runs:
        df = pandas.read_csv(runs)
        list_survivaltimes = df["survival time"]
        list_survivaltimes =  pandas.to_numeric(list_survivaltimes, errors="coerce")
        print(list_survivaltimes)
