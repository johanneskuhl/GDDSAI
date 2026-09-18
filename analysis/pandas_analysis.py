import csv

import os

import pandas

if os.path.isfile("data/runs.csv"):
    with open("data/runs.csv", "r") as runs:
        df = pandas.read_csv(runs)
        dict_survivaltimes = df["survival time"]
        dict_survivaltimes =  pandas.to_numeric(dict_survivaltimes, errors="coerce")
        pogingen = dict_survivaltimes.count()
        gemiddelde_st = dict_survivaltimes.sum() / pogingen
        best_attempt = 0
        max_st = 0
        for pogingnummer, survtime in dict_survivaltimes.items():
            if survtime > max_st:
                max_st = survtime
                best_attempt = pogingnummer
        print(f"attempts: {pogingen}, average survival time: {gemiddelde_st}, best attempt: attempt {best_attempt} survival time {max_st}")
        print(dict_survivaltimes)