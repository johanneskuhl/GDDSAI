import csv  

import os

import matplotlib.pyplot as plt

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
    # print message and data
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

    # graph
    plotsurvtime = []
    attempts = []
    for attempt, plot_st in survtime_dict.items():
        attempts.append(attempt)
        plotsurvtime.append(plot_st)
    fig, ax = plt.subplots()
    ax.plot(attempts, plotsurvtime, marker='o', label="Data Points")

    ax.set_title("survival times")
    ax.set_xlabel("attempt")
    ax.set_ylabel("survival time")

    ax.legend()
    plt.show()