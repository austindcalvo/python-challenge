#import
import os
import csv
import re

poll_csv = os.path.join("/Users/austindcalvo/UTSAGithub/python-challenge/PyPoll/Resources/election_data.csv")
with open(poll_csv, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)

    #variables

    votes_cast = []
    candidate_list = []
    counties = []

    #Candidates
    Stockham = []
    Degette = []
    Doane = []

    #Votes
    Stockham_Votes = 0
    Degette_Votes = 0
    Doane_Votes = 0


    for row in csv_reader:
        votes_cast.append(int(row[0]))
        counties.append(row[1])
        candidate_list.append(row[2])

    vote_count = (len(votes_cast))

    for candidate in candidate_list:
        if re.search('Stockham', candidate):
            Stockham.append(candidate_list)
            Stockham_Votes = len(Stockham)

        elif re.search('DeGette', candidate):
            Degette.append(candidate_list)
            Degette_Votes = len(Degette)
        else:
            Doane.append(candidate)
            Doane_Votes = len(Doane)

    Stockham_percent = round(((Stockham_Votes / vote_count) * 100), 3)
    Degette_percent = round(((Degette_Votes / vote_count) * 100), 3)
    Doane_percent = round(((Doane_Votes / vote_count) * 100), 3)

    if Stockham_percent > 50 :
        winner = "Charles Casper Stockham"
    elif Degette_percent > 50 :
        winner = "Diana DeGette"
    elif Doane_percent > 50 :
        winner = "Raymon Anthony Doane"
    else:
        winner = max(Stockham_percent,Degette_percent,Doane_percent)

print("Election Results")
print("-------------------------")
print("Total Votes:", vote_count)
print("-------------------------")
print("Charles Casper Stockham: ", Stockham_percent,"%"," (", Stockham_Votes,")")
print("Diana DeGette: ", Degette_percent,"%"," (", Degette_Votes,")")
print("Raymon Anthony Doane: ", Doane_percent,"%"," (", Doane_Votes,")")
print("-------------------------")
print("Winner: ", winner)
print("-------------------------")

file = open("PyPoll.txt","w")
file.write("Election Results" + "\n")
file.write("-------------------------" + "\n")
file.write("Total Votes:" + str(vote_count) + "\n")
file.write("-------------------------" + "\n")
file.write("Charles Casper Stockham: " + str(Stockham_percent)+"%" + " (" + str(Stockham_Votes)+ ")" + "\n")
file.write("Diana DeGette: " + str(Degette_percent)+"%" + " (" + str(Degette_Votes)+ ")" + "\n")
file.write("Raymon Anthony Doane: " + str(Doane_percent)+"%" + " (" + str(Doane_Votes)+ ")" + "\n")
file.write("-------------------------" + "\n")
file.write("Winner: "+ str(winner) + "\n")
file.write("-------------------------" + "\n")

file.close()