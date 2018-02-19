"""
Assignment:  Homework 3
Option 1:  PyPoll
Author:  Patrick Humphries
Orgainization:  USC Viterbi Analytics Bootcamp, 1/30

In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. 

(Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, 
his concentration isn't what it used to be.)

You will be given two sets of poll data (election_data_1.csv and election_data_2.csv). 
Each dataset is composed of three columns: Voter ID, County, and Candidate. 
Your task is to create a Python script that analyzes the votes and calculates each of the following:
•	The total number of votes cast
•	A complete list of candidates who received votes
•	The percentage of votes each candidate won
•	The total number of votes each candidate won
•	The winner of the election based on popular vote.


"""
import election_processor

election_processor.run()
