<<<<<<< HEAD
"""
Module:  election_processor.py
Author:  Patrick Humphries
Orgainization:  USC Viterbi Analytics Bootcamp, 1/30
Output:  Election Results are written to screen and text file.
Methods:  run()
Description:
    1.  Read the input csv files.
    2.  Build a election model with aggregated votes by candidate.
    3.  Print and write aggregates per candidate.
    4.  Print the name of the winner.
"""
import election_factory
import os

def run():
    # Select all csv files in the current directory to process.
    # Assumption:  csv file names start with "election_data_"
    file_names = []
    directory_entries = os.listdir()
    for directory_entry in directory_entries:
        if directory_entry.startswith("election_data_"):
            if directory_entry.endswith(".csv"):
                file_names.append(directory_entry)

    # Get the election model created from the input csv files.
    election_model = election_factory.get_election_model(file_names)

    # Write election to the screen and text file using the election model as the source.
    with open("election_results.txt", "w") as report_file:
    
        report_line = "\n-------------------------------"
        print(report_line)
        report_file.write(report_line)

        report_line = "\nTotal Votes:  {:,.0f}".format(election_model["total_votes"])
        print(report_line)
        report_file.write(report_line)

        report_line = "\n-------------------------------"
        print(report_line)
        report_file.write(report_line)

        candidates = election_model["candidates"]

        names = candidates.keys()
        name_list = list(names)
        name_list.sort()

        for name in name_list:   
            candidate = candidates[name]
            cp = candidate["percentage"]
            ct = candidate["votes"]
            report_line = "\n{}: {:,.1f}% ({:,.0f})".format(name, cp, ct)
            print(report_line)
            report_file.write(report_line)

        report_line = "\n-------------------------------"
        print(report_line)
        report_file.write(report_line)

        candidate = election_model["winner"]
        cw = election_model["winner"]
        report_line = "\nWinner: {}".format(cw)
        print(report_line)
        report_file.write(report_line)

        report_line = "\n-------------------------------"
        print(report_line)
        report_file.write(report_line)

        input("Press Enter to continue.")
=======
"""
Module:  election_processor.py
Author:  Patrick Humphries
Orgainization:  USC Viterbi Analytics Bootcamp, 1/30
Output:  Election Results are written to screen and text file.
Methods:  run()
Description:
    1.  Read the input csv files.
    2.  Build a election model with aggregated votes by candidate.
    3.  Print and write aggregates per candidate.
    4.  Print the name of the winner.
"""
import election_factory
import os

def run():
    # Select all csv files in the current directory to process.
    # Assumption:  csv file names start with "election_data_"
    file_names = []
    directory_entries = os.listdir()
    for directory_entry in directory_entries:
        if directory_entry.startswith("election_data_"):
            if directory_entry.endswith(".csv"):
                file_names.append(directory_entry)

    # Get the election model created from the input csv files.
    election_model = election_factory.get_election_model(file_names)

    # Write election to the screen and text file using the election model as the source.
    with open("election_results.txt", "w") as report_file:
    
        report_line = "\n-------------------------------"
        print(report_line)
        report_file.write(report_line)

        report_line = "\nTotal Votes:  {:,.0f}".format(election_model["total_votes"])
        print(report_line)
        report_file.write(report_line)

        report_line = "\n-------------------------------"
        print(report_line)
        report_file.write(report_line)

        candidates = election_model["candidates"]

        names = candidates.keys()
        name_list = list(names)
        name_list.sort()

        for name in name_list:   
            candidate = candidates[name]
            cp = candidate["percentage"]
            ct = candidate["votes"]
            report_line = "\n{}: {:,.1f}% ({:,.0f})".format(name, cp, ct)
            print(report_line)
            report_file.write(report_line)

        report_line = "\n-------------------------------"
        print(report_line)
        report_file.write(report_line)

        candidate = election_model["winner"]
        cw = election_model["winner"]
        report_line = "\nWinner: {}".format(cw)
        print(report_line)
        report_file.write(report_line)

        report_line = "\n-------------------------------"
        print(report_line)
        report_file.write(report_line)

        input("Press Enter to continue.")
>>>>>>> a46ccf54e7cdc6f82cafbdeccdfc490c67d6f4a7
