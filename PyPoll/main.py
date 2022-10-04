import csv
import os


candidate_list = [] # list of unique candidates
percent_list = []
candidate_dict = {}
candidate_votes = []
total_votes = 0

polldata_csv = os.path.join("Resources", "election_data.csv")

# Open and read csv
with open(polldata_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")

    for row in csv_reader:
        total_votes += 1
        candidate_list.append(row[2])
        if row[2] not in candidate_votes:
            candidate_votes.append(row[2])
    
    total_votes -=1

for i in range (len(candidate_votes)):
    counter =0
    for j in range(len(candidate_list)):
        if candidate_votes[i] == candidate_list[j]:
            counter +=1
    candidate_dict[candidate_votes[i]] = counter
candidate_votes.remove('Candidate')

f= open("PyPoll_results.txt", 'w')
f.write ('Election Results\n')
print ('Election Results')
f.write ('Total Votes:  ' + str(total_votes) + '\n')
print ('Total Votes:  ' + str(total_votes))
for i in candidate_votes:
    f.write (i)
    f.write(' '+ str(round((candidate_dict[i]/total_votes) * 100,3)) + '%')
    f.write(' (' + str(candidate_dict[i]) + ')\n')
    print (i, str(round((candidate_dict[i]/total_votes) * 100,3)) + '%', '(' + str(candidate_dict[i]) + ')')


max_no_votes = max(candidate_dict.values())
winner = [k for k, v in candidate_dict.items() if v == max_no_votes]

f.write ('Winner: ' + str(winner).strip('[]').strip(''))
print ('Winner: ' + str(winner).strip('[]').strip(''))


f.close()
