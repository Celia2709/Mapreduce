#Redefine o mapper e o reducer de xeito que devolvan un
#  ficheiro co total de vendas por categoría.


import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    date, time, store, item, cost, payment = data
    print(item+"\t"+cost)
