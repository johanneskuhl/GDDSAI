import csv

survivaltime_list = []


with open("data/runs.csv", "r") as runs:
    csvreader = csv.reader(runs)

    next(csvreader)

    for row in csvreader:
        survivaltime_list.append(float(row[0]))

if len(survivaltime_list) == 0:
    print("no attempts made yet")
else:
    pogingen = len(survivaltime_list)
    gemiddelde_st = sum(survivaltime_list) / pogingen
    min_st = min(survivaltime_list)

    best_attempt, max_st = 1, survivaltime_list[0]
    for i, v in enumerate(survivaltime_list):
        if v >= max_st:
            best_attempt, max_st = i, v

    print(f"attempts: {pogingen}, average survival time: {gemiddelde_st}, best attempt: attempt {best_attempt} survival time {max_st})")
