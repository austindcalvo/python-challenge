import os
import csv
import locale

budget_csv = os.path.join("/Users/austindcalvo/UTSAGithub/python-challenge/PyBank/Resources/budget_data.csv")

with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
filename = open("/Users/austindcalvo/UTSAGithub/python-challenge/PyBank/Resources/budget_data.csv")
file = csv.DictReader(filename)
date_records = list(file)

month = []
pl = []
plcorrected = list(map(int, pl))