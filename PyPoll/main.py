#My Dependencies
import csv
from functools import total_ordering
import os

#Files to load and output
election_data = "PyPoll/Resources/election_data.csv"
voter_output = "PyPoll/electionanalysis/electionanalysis.txt"

#Total Vote Counter
total_votes = 0

#Candidate options and vote counters
candidate_options = [] 
candidate_votes = {}

#Winning candidate andnning count tracker
winning_candidate = ""
winning_count = 0

#Read csv and convert to list of dictionaries
with open(election_data) as election_data:
    reader = csv.reader(election_data)

    header = next(reader)

    #Do for each row
    for row in reader:

        print(". ", end=""),

        #Add to total vote count
        total_votes = total_votes + 1

        #Get candidate name from each row
        candidate_name = row[2]

        #if candidate does not match any existing candidate
        if candidate_name not in candidate_options:

            #Add it to my list of candidates in the running
            candidate_options.append(candidate_name)

            #And begin tracking that candidates votes count
            candidate_votes[candidate_name] = 0

        #Then add a vote to that candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1 

    #Print the results and export data to text file
    with open(election_data, "w") as election_data:

    #Print final vote count
        election_results =  (
            f"\n\nElection Results\n"
            f"----------------------------\n"
            f"Total Votes: {total_votes}\n"
            f"----------------------------\n")
        print(election_results, end="")    
            
    

    #Save final vote count to text file
    txt_file.write(election_results)

    #Find winner by looping through all counts
    for candidate in candidate_votes:

        #Retrieve the vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        #Determine winning vote count and the candidate's name
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        #Print each candidates voter count and percentage
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

       #Save each candidates voter count and percentage to text file
        txt_file.write(voter_output)

    #Print the winning candidate
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"---------------------------\n"
    )
    print(winning_candidate_summary)

    #Save Winner's name to text file
    txt_file.write(winning_candidate_summary)
            