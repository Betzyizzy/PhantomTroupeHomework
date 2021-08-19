import os
import csv

csvpath = "Resources\\election_data.csv"

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    
    all_rows = []
    for row in csvreader:
        all_rows.append(row)

    total_voters = len(all_rows)    


    voter_count = {}
    percent = {}

    for row in all_rows:
        if row[2] not in voter_count:
            voter_count[row[2]] = 1
        else:
            voter_count[row[2]] += 1

    for key in voter_count:
        percent[key] = voter_count[key] / total_voters 

    mostVotes = max(percent,key=percent.get)

    print(f"Election Results")
    print(f"-------------------------")
    print(f"Total Votes: {total_voters}")
    print(f"-------------------------")
    print(f"Khan: {round(percent['Khan']*100)}% ({voter_count['Khan']})")
    print(f"Correy: {round(percent['Correy']*100)}% ({voter_count['Correy']})")
    print(f"Li: {round(percent['Li']*100)}% ({voter_count['Li']})")
    print(f"O'Tooley: {round(percent['''O'Tooley''']*100)}% ({voter_count['''O'Tooley''']})")
    print(f"-------------------------")
    print(f"Winner: {mostVotes}")
    print(f"-------------------------")

out_path = "pypoll.txt"
with open(out_path, "w") as text:
    text.write(f"Election Results\n")
    text.write(f"-------------------------\n")
    text.write(f"Total Votes: {total_voters}\n")
    text.write(f"-------------------------\n")
    text.write(f"Khan: {round(percent['Khan']*100)}% ({voter_count['Khan']})\n")
    text.write(f"Correy: {round(percent['Correy']*100)}% ({voter_count['Correy']})\n")
    text.write(f"Li: {round(percent['Li']*100)}% ({voter_count['Li']})\n")
    text.write(f"O'Tooley: {round(percent['''O'Tooley''']*100)}% ({voter_count['''O'Tooley''']})\n")
    text.write(f"-------------------------\n")
    text.write(f"Winner: {mostVotes}\n")
    text.write(f"-------------------------\n")