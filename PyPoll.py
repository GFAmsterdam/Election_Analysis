#Add our Dependencies
import csv
import os
#Assign a variable to load file from a path
file_to_load = os.path.join("Election_Analysis","Resources", "election_results.csv")
#Assign a variable to save the file to a path
file_to_save = os.path.join("Election_Analysis", "Resources", "election_analysis.txt")
#1. Initialize a Total Vote Counter.
total_votes = 0
#candidate Options and Votes
candidate_options = []
candidate_votes = {} 
#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#Open election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #Read the Header Row
    headers = next(file_reader)
    #Print each row in the CSV file.
    for row in file_reader:
        #2. Add to the total vote count.
        total_votes += 1
        #Get candidate name from each row
        candidate_name = row[2]
        #If the candidate does not match any existing cadidate
        if candidate_name not in candidate_options:
            #Add it tot he list of candidates
            candidate_options.append(candidate_name)

            #2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        #Add a vote count to that candidates count.
        candidate_votes[candidate_name] += 1

    with open(file_to_save, "w") as txt_file:
        #print the final vote count to the terminal
        election_results = (
            f"\nElection Results\n"
            f"------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"--------------------------\n")
        print(election_results, end="")
        
        #Save the final vote count to the text file
        txt_file.write(election_results)
        #Determine the percentage of votes for each candidate by looping through the counts
        #1. Iterate through the candidate list
        for candidate_name in candidate_votes:
            #2. Retreive vote count of candidate
            votes = candidate_votes[candidate_name]
            #3. calculate the percentage of votes
            vote_percentage = float(votes) / float(total_votes) * 100
            #4. Print the candidate names and percentage of votes
            candidate_results = (
            f"{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n")
            txt_file.write(candidate_results)
            #to do: print out each candidates name, vote count, and percentage of votes to terminal

            #Determine winning vote count and candidate
            #Determine if the votes are greater than the winning count
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                #If True then set winning_count = votes and winning_percentage = vote_percentage
                winning_count = votes
                winning_percentage - vote_percentage
                #And set the winning_candidate equal to the candidates name
                winning_candidate = candidate_name 
            
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"---------------------------\n")
        print(winning_candidate_summary)
        #Save the winning candidate's name to the text file
        txt_file.write(winning_candidate_summary)

    
    






