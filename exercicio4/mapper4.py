import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    date, time, store, item, cost, payment = data
    print(cost)
