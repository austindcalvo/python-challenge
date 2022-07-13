import os
import csv
import locale
import decimal

budget_csv = os.path.join("/Users/austindcalvo/UTSAGithub/python-challenge/PyBank/Resources/budget_data.csv")

 #Open and read csv
with open(budget_csv,newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
filename = open("/Users/austindcalvo/UTSAGithub/python-challenge/PyBank/Resources/budget_data.csv")
file = csv.DictReader(filename)




#PL and Months
month = []
pl = []
plcorrected = list(map(int, pl))

#iterating over each row and append
# values to empty list
for col in file:
    month.append(col['Date'])
    pl.append(col['Profit/Losses'])
    plcorrected.append(col['Profit/Losses'])

#pl Change
pl_change = []

for a in range(1, len(pl)):
    pl_change.append((int(pl[a]) - int(pl[a-1])))

#avg change

avg_change = sum(pl_change) / len(month)


number_of_months = len(month)
number_of_pl = len(pl)
total_pl = sum(list(map(int, plcorrected)))
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

max_inc = max(pl_change)

min_inc = min(pl_change)


    #print("Month:", month)
print("Financial Analysis")
print("----------------------------")
print("Total Months:", number_of_months)
print("Average Change: ", locale.currency(avg_change))
print("Total:",locale.currency(total_pl))
print("Greatest Increase in Profits: ", str(month[pl_change.index(max(pl_change)) + 1]),locale.currency((max_inc)))
print("Greatest Decrease in Profits: ", str(month[pl_change.index(min(pl_change)) + 1]),locale.currency((min_inc)))



#write to file
file = open("PyBank.txt","w")
file.write("Financial Analysis" + "\n")
file.write("----------------------------" + "\n")
file.write("Total Months:" + str(number_of_months) + "\n")
file.write("Average Change: "+ str(locale.currency(avg_change)) + "\n")
file.write("Total:"+ str(locale.currency(total_pl)) + "\n")
file.write("Greatest Increase in Profits: "+ str(month[pl_change.index(max(pl_change)) + 1]) + " (" + str(locale.currency((max_inc))) + ")\n")
file.write("Greatest Decrease in Profits: "+ str(month[pl_change.index(min(pl_change)) + 1]) + " (" + str(locale.currency((min_inc))) + ")\n")
file.close()




#----------------------------------------------
#print(number_of_pl)
#print(average)


#Open and read csv
#with open(budget_csv,"r") as csv_file:
    #csv_reader = csv.reader(csv_file, delimiter=",")
   # headings=next(csv_reader)
#filename = open("/Users/austindcalvo/UTSAGithub/python-challenge/PyBank/Resources/budget_data.csv")
#file = csv.DictReader(filename)
#date_records = list(file)

#for Dates in date_records:
   # new_maximum_val = max(Dates.keys(), key=(lambda new_k: Dates[new_k]))
   # print('Maximum Value: ', Dates[new_maximum_val])
   # new_minimum_val = min(Dates.keys(), key=(lambda new_k: Dates[new_k]))
   # print('Minimum Value: ', Dates[new_minimum_val])

    #all_pairs = list(Dates.items())
    #print(max(all_pairs))



#all_pairs = list(Dates.items())
#print('First Key value pair: ', all_pairs)
