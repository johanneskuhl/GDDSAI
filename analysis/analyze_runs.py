import csv  

import os

survivaltime_list = []

if os.path.isfile("data/runs.csv"):
    with open("data/runs.csv", "r") as runs:
        csvreader = csv.reader(runs)

        next(csvreader, None)

        for row in csvreader:
            if len(row) != 3:
                continue
            try:
                survtime = float(row[0])
            except ValueError:
                continue
            if survtime >= 0:
                survivaltime_list.append(survtime)

if len(survivaltime_list) == 0:
    print("no correct attempts made yet")
else:
    pogingen = len(survivaltime_list)
    gemiddelde_st = sum(survivaltime_list) / pogingen
    min_st = min(survivaltime_list)

    best_attempt, max_st = 1, survivaltime_list[0]
    for i, v in enumerate(survivaltime_list, start=1):
        if v > max_st:
            best_attempt, max_st = i, v

    print(f"attempts: {pogingen}, average survival time: {gemiddelde_st}, best attempt: attempt {best_attempt} survival time {max_st}")
    print(survivaltime_list)