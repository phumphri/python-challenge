"""
Module:  election_factory.py
Author:  Patrick Humphries
Organization:  USC Viterbi Analytics Boot Camp, January 30, 2018
Description:  Provide an election model which provides aggregated values from
    multiple csv files.
Assumptions:
    1. Input files will be regular CSV files.
    2. First row will be a header.
    3. Columns are Voter ID, County, Candidate
Methods:
    get_election_model(file_names)
"""
import csv

def get_election_model(file_names):
    """
    Module:  election_factory
    Function:  get_election_model
    Parameter:  File name of a CSV file with election data.
    Return:  Election Model, type dict, containing aggregated election data.
    """
    # Define Eelection Model
    # {
    #   "candidates": candidates,
    #   "winner": winner
    # }
    election_model = {}
    election_model["number_of_candidates"] = 0
    election_model["total_votes"] = 0

    # Each candidate in candidates contains aggregated information for that candidate.
    # {
    #   "name": candidate
    # }
    candidates = {}
    election_model["candidates"] = candidates

    # Each candidate has attributes.
    # {
    #   "name": name
    #   "percentage": percentage (aggregated)
    #   "votes": votes (aggregated)
    # }

    # Process each csv file found in the list argument.
    for file_name in file_names:
        try:
            # Process the csv file.
            with open(file_name, 'r', encoding='ascii') as csv_file:

                # Create a reader for the CSV file.
                csv_reader = csv.reader(csv_file, delimiter=',')

                process_rows(csv_reader, election_model)

        except FileNotFoundError as error:
            print('\nIn election_model.py a ' \
                    'FileNotFoundError was thrown for file {}.'.format(file_name))
            print('FileNotFoundError.args:')
            for arg in error.args:
                print('\t', arg)
            print('\n')
            exit(1)

        except IOError as error:
            print('\nIn election_model.py a ' \
                    'IOError was thrown for file {}.'.format(file_name))
            print('FileNotFoundError.args:')
            for arg in error.args:
                print('\t', arg)
            print('\n')
            exit(1)

    # Sort and aggregate candidates.
    sort_and_aggregate_candidates(election_model)

    # Return budgt model containing aggregated amounts.
    return election_model

def process_rows(csv_reader, election_model):
    """
    For each row in the csv_reader, either add or update the candidate in the election model.
    The candidate key will be used for processing the election model in alphbetical order.
    """
    # Metadata
    voter_id_column = 0
    name_column = 2

    i = 0   # Unit Tesing

    for row in csv_reader:

        # Unit Testing
        # i = i + 1
        # if i > 4:
        #     break

        voter_id_string = str(row[voter_id_column])

        # Bypass header.
        if voter_id_string == "Voter ID":
            continue
    
        # Get candidate's name.
        name = row[name_column]

        # If the candidate already exists, add the vote to the candidate's votes.
        # If the candidate does not exist, add the candidate with their vote.
        candidates = election_model["candidates"]

        if name in candidates:
            candidate = candidates[name]
            candidate["votes"] = candidate["votes"] + 1
        else:
            candidate = {}
            candidate["percentage"] = 0
            candidate["votes"] = 1
            candidates[name] = candidate

        election_model["total_votes"] = election_model["total_votes"] + 1

    
def sort_and_aggregate_candidates(election_model):
    """
    Calculate aggregations by processing the election model in chronological order.
    """
    # Count the number of candidates
    candidates = election_model["candidates"]      
    number_of_candidates = len(candidates)    
    election_model["number_of_candidates"] = number_of_candidates

    # Get the reference to the total votes in the election model.
    total_votes = election_model["total_votes"]

    # Initialize the winner.
    winner_name = "nobody"
    winner_votes = 0

    # Retrieve sort keys for election model and sort them into chronological order.
    names = candidates.keys()
    name_list = list(names)
    name_list.sort()

    # Calculate aggregations by processing candidates in alphbetic order.
    for name in name_list:

        candidate = candidates[name]

        votes = candidate["votes"]

        candidate["percentage"] = (votes / election_model["total_votes"]) * 100
        
        if votes > winner_votes:
            winner_votes = votes
            winner_name = name

    # Write aggregations to the election model.
    election_model["winner"] = winner_name
