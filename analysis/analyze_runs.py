import csv  

import os

survtime_dict = {}

if os.path.isfile("data/runs.csv"):
    with open("data/runs.csv", "r") as runs:
        csvreader = csv.reader(runs)

        next(csvreader, None)

        for pogingnummer, row in enumerate(csvreader, start=1):
            if len(row) < 3:
                continue
            try:
                survtime = float(row[0])
            except ValueError:
                continue
            if survtime >= 0:
                survtime_dict[pogingnummer] = survtime
            

if len(survtime_dict) == 0:
    print("no correct attempts made yet")
else:
    pogingen = len(survtime_dict)
    gemiddelde_st = sum(survtime_dict.values()) / pogingen
    best_attempt = 0
    max_st = 0
    for pogingnummer, survtime in survtime_dict.items():
        if survtime > max_st:
            max_st = survtime
            best_attempt = pogingnummer

    print(f"attempts: {pogingen}, average survival time: {gemiddelde_st}, best attempt: attempt {best_attempt} survival time {max_st}")
    print(survtime_dict)