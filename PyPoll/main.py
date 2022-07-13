import os
import csv
with open('Resources', 'budget_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
