import os
import csv

csvpath = "budget_data.csv"

#Total Months
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvfile)
    months = sum(1 for row in csvreader)

#Total
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvfile)
    total = sum(int(row[1]) for row in csvreader)

#Revenue
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvfile)
    revenue = list(int(row[1]) for row in csvreader)

#Dates
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvfile)
    date = list(row[0] for row in csvreader)

#Greatest Increase/Decrease
rev_change = []
for i in range(len(revenue)-1):
    rev_change.append(revenue[i+1] - revenue[i])

greatest_increase = max(rev_change)
greatest_decrease = min(rev_change)

date_of_great_inc = date[rev_change.index(greatest_increase)+1]
date_of_great_dec = date[rev_change.index(greatest_decrease)+1]

#Average Change
avg_change = round(sum(rev_change) / len(rev_change), 2)

print(f"Financial Analysis\n----------------------------\nTotal Months: {months}\nTotal: ${total}\nAverage Change: ${avg_change}\nGreatest Increase in Profits: {date_of_great_inc} (${greatest_increase})\nGreatest Decrease in Profits: {date_of_great_dec} (${greatest_decrease})")

f = open('PyBank.txt','w')
f.write(f"Financial Analysis\n----------------------------\nTotal Months: {months}\nTotal: ${total}\nAverage Change: ${avg_change}\nGreatest Increase in Profits: {date_of_great_inc} (${greatest_increase})\nGreatest Decrease in Profits: {date_of_great_dec} (${greatest_decrease})")
f.close()
