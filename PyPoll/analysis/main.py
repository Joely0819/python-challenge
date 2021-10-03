#import dependencies
import os
#import module for reading CSV Files
import csv
#specify file path
FilePath = os.path.join('Resources', 'election_data.csv')

# The total number of votes cast
#Variables
All_Votes = 0
Correy_Votes = 0
Khan_Votes = 0
Li_Votes = 0
Tooley_Votes = 0

#open csv file
with open(FilePath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#skip header
    header = next (csvreader)

#Go through rows
    for row in csvreader:
        All_Votes +=1
#complete candidate list
        if row[2] == 'Correy':
            Correy_Votes +=1
        elif row[2] == 'Khan':
            Khan_Votes +=1
        elif row[2] == 'Li':
            Li_Votes +=1
        elif row[2] == "O'Tooley":
            Tooley_Votes +=1
#Find winner through dictionary and the total number of votes each candidate won

#key values 
candidates = ['Correy', 'Khan', 'Li', 'Tooley']
votes = [Correy_Votes, Khan_Votes, Li_Votes, Tooley_Votes]
#use dictionary
candidates_votes = dict(zip(candidates, votes))
#find winner
winner = max(candidates_votes, key=candidates_votes.get)

#   The percentage of votes each candidate won
Correy_percentage = (Correy_Votes/All_Votes) *100
Khan_percentage = (Khan_Votes/All_Votes) *100
Li_percentage = (Li_Votes/All_Votes) *100
Tooley_percentage = (Tooley_Votes/All_Votes) *100

#Print
print(f'Election Results')
print(f'--------------------')
print(f'Total Votes: {All_Votes}')
print(f'--------------------')
print(f'Khan: {Khan_percentage:.3f}% ({Khan_Votes})')
print(f'Correy: {Correy_percentage:.3f}% ({Correy_Votes})')
print(f'Li: {Li_percentage:.3f}% ({Li_Votes})')
print(f"O'Tooley: {Tooley_percentage:.3f}% ({Tooley_Votes})")
print(f'--------------------')
print(f'Winner: {winner}')
print(f'--------------------')

# write to text
txt_file = os.path.join('analysis', 'PyPollTXT')
with open('txt_file', "w") as text:
    text.write(f'Election Results')
    text.write('\n')
    text.write('-----------------')
    text.write('\n')
    text.write(f'Total Votes: {All_Votes}')
    text.write('\n')
    text.write('-----------------')
    text.write('\n')
    text.write(f'Khan: {Khan_percentage:.3f}% ({Khan_Votes})')
    text.write('\n')
    text.write(f'Correy: {Correy_percentage:.3f}% ({Correy_Votes})')
    text.write('\n')
    text.write(f'Li: {Li_percentage:.3f}% ({Li_Votes})')
    text.write('\n')
    text.write(f"O'Tooley: {Tooley_percentage:.3f}% ({Tooley_Votes})")
    text.write('\n')
    text.write(f'--------------------')
    text.write('\n')
    text.write(f'Winner: {winner}')
    text.write('\n')
    text.write(f'--------------------')
