import os
import csv
#print(os.getcwd)
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

votes = []
candidateList = []

with open(csvpath) as csvfile:
    #read header
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    #get list of votes by last name
    for row in csvreader:
        votes.append(row[2])

num_votes = len(votes)

#get list of candidates        
for candidate in votes:
    if candidate not in candidateList:
        candidateList.append(candidate)
#print(candidateList)
KhanVotes = 0
CorreyVotes = 0
LiVotes = 0
OTooleyVotes = 0

#Get numner of votes for each candidate
for candidate in votes:
    if candidate == "Khan":
       KhanVotes = KhanVotes + 1
    if candidate == "Correy":
       CorreyVotes = CorreyVotes + 1
    if candidate == "Li":
       LiVotes = LiVotes + 1
    if candidate == "O'Tooley":
       OTooleyVotes = OTooleyVotes + 1

#Calculate percent of votes for each candidate
Khan_percent = (KhanVotes / num_votes) * 100
Correy_percent = (CorreyVotes / num_votes) * 100
Li_percent = (LiVotes / num_votes) * 100
OTooley_percent = (OTooleyVotes / num_votes) * 100

#determine winner
if KhanVotes > CorreyVotes and KhanVotes > LiVotes and KhanVotes > OTooleyVotes:
    winner = "Khan"
elif CorreyVotes > KhanVotes and CorreyVotes > LiVotes and CorreyVotes > OTooleyVotes:
    winner = "Correy"
elif LiVotes > KhanVotes and LiVotes  > CorreyVotes and LiVotes  > OTooleyVotes:
    winner = "Li"
elif OTooleyVotes  > KhanVotes and OTooleyVotes  > CorreyVotes and OTooleyVotes  > LiVotes:
    winner = "O'Tooley"

#Print results in terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes:  {num_votes} ")
print("-------------------------")
print(f"Khan: {round(Khan_percent, 3)}% ({KhanVotes})")
print(f"Correy: {round(Correy_percent, 3)}% ({CorreyVotes})")
print(f"Li: {round(Li_percent, 3)}% ({LiVotes})")
print(f"O'Tooley: {round(OTooley_percent, 3)}% ({OTooleyVotes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#PyPoll_results = open(Python-Challenge/PyPoll/main.py/PyPoll_results.txt)
#with open((os.path.join("~", "Python-Challenge", "PyPoll", "PyPoll_results.txt")), "w") as PyPoll_results:


#Print results to .txt
with open("PyPoll_results.txt", "w") as PyPoll_results:
    PyPoll_results.write(f"""
    Election Results
    -------------------------
    Total Votes:  {num_votes} 
    -------------------------
    Khan: {round(Khan_percent, 3)}% ({KhanVotes})
    Correy: {round(Correy_percent, 3)}% ({CorreyVotes})
    Li: {round(Li_percent, 3)}% ({LiVotes})
    O'Tooley: {round(OTooley_percent, 3)}% ({OTooleyVotes})
    -------------------------
    Winner: {winner}
    -------------------------""")
