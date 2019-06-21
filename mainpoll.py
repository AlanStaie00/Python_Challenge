import os
import csv

csvpath = "election_data.csv"

#Save each col to variable
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvfile)

    voter_id = []
    country = []
    candidate = []

    for row in csvreader:
        voter_id.append(row[0])
        country.append(row[1])
        candidate.append(row[2])


total_votes = len(voter_id)
cand_with_votes = list(set(candidate))

tooley_votes = sum(1 for i in candidate if i==cand_with_votes[0])
khan_votes = sum(1 for i in candidate if i==cand_with_votes[1])
li_votes = sum(1 for i in candidate if i==cand_with_votes[2])
correy_votes = sum(1 for i in candidate if i==cand_with_votes[3])

tallied_votes = [tooley_votes, khan_votes, li_votes, correy_votes]

tooley_pct = round(tooley_votes/total_votes * 100, 1)
khan_pct = round(khan_votes/total_votes * 100, 1)
li_pct = round(li_votes/total_votes * 100, 1)
correy_pct = round(correy_votes/total_votes * 100, 1)

pct_votes = [tooley_pct, khan_pct, li_pct, correy_pct]

cand_with_votes = [x for _,x in sorted(zip(tallied_votes,cand_with_votes),reverse = True)]
tallied_votes.sort(reverse=True)
pct_votes.sort(reverse=True)

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"{cand_with_votes[0]}: {pct_votes[0]}% ({tallied_votes[0]})")
print(f"{cand_with_votes[1]}: {pct_votes[1]}% ({tallied_votes[1]})")
print(f"{cand_with_votes[2]}: {pct_votes[2]}% ({tallied_votes[2]})")
print(f"{cand_with_votes[3]}: {pct_votes[3]}% ({tallied_votes[3]})")
print("-------------------------")
print(f"Winner: {cand_with_votes[0]}")

f = open('PyPoll.txt','w')
f.write("Election Results\n")
f.write("-------------------------\n")
f.write(f"Total Votes: {total_votes}\n")
f.write("-------------------------\n")
f.write(f"{cand_with_votes[0]}: {pct_votes[0]}% ({tallied_votes[0]})\n")
f.write(f"{cand_with_votes[1]}: {pct_votes[1]}% ({tallied_votes[1]})\n")
f.write(f"{cand_with_votes[2]}: {pct_votes[2]}% ({tallied_votes[2]})\n")
f.write(f"{cand_with_votes[3]}: {pct_votes[3]}% ({tallied_votes[3]})\n")
f.write("-------------------------\n")
f.write(f"Winner: {cand_with_votes[0]}\n")
f.close()
