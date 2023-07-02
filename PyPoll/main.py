import os
import csv
csv_file = os.path.join("Resources", "election_data.csv")

column_name = 'Candidate'
vote_counter = 0
candidate_name = []
cand = 0
cand1 = 0
cand2 = 0
name = "x"
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        vote_counter = vote_counter + 1
        if name != row[column_name]:
            candidate = row[column_name]
            if candidate not in candidate_name:
                candidate_name.append(candidate)
            name = candidate
        if row[column_name] == candidate_name[0]:
            cand = cand + 1
        elif row[column_name] == candidate_name[1]:
            cand1 = cand1 + 1
        elif row[column_name] == candidate_name[2]:
            cand2 = cand2 + 1


   
cand_percent = round((cand/vote_counter) * 100,3)        
cand1_percent = round((cand1/vote_counter) * 100,3)  
cand2_percent = round((cand2/vote_counter) * 100,3)

for person in candidate_name:
    if cand_percent > cand1_percent and cand_percent > cand2_percent:
        winner = candidate_name[0]
    elif cand1_percent > cand_percent and cand1_percent > cand2_percent:
        winner = candidate_name[1]
    elif cand2_percent > cand_percent and cand2_percent > cand1_percent:
        winner = candidate_name[2]
        
print("Election Results")
print("-------------------------")
print(f"Total Votes: {vote_counter}")
print("-------------------------")
print(f"{candidate_name[0]}: {cand_percent}% ({cand})")
print(f"{candidate_name[1]}: {cand1_percent}% ({cand1})")   
print(f"{candidate_name[2]}: {cand2_percent}% ({cand2})")  
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

txt_file = os.path.join("Analysis", "results.txt")
with open(txt_file, 'w') as f:
    f.write("Election Results\n")
    f.write("-------------------------\n")
    f.write(f"Total Votes: {vote_counter}\n")
    f.write("-------------------------\n")
    f.write(f"{candidate_name[0]}: {cand_percent}% ({cand})\n")
    f.write(f"{candidate_name[1]}: {cand1_percent}% ({cand1})\n")   
    f.write(f"{candidate_name[2]}: {cand2_percent}% ({cand2})\n")  
    f.write("-------------------------\n")
    f.write(f"Winner: {winner}\n")
    f.write("-------------------------\n")