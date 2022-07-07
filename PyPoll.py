# The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote
#Assign a variable for the file to load and the path
#Add our dependencies
import csv
import os
#Assign a variable to load file from a path
file_to_load = os.path.join("Election_Analysis","Resources", "election_results.csv")
#Assign a variable to save the file to a path
file_to_save = os.path.join("Election_Analysis", "Resources", "election_results.txt")
#Open election results and read the file
with open(file_to_load) as election_data:

    #To do : read and analyze data here
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)
    #Read and Print the Header Row.
    headers = next(file_reader)
    print(headers)

    
    






