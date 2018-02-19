<<<<<<< HEAD
"""
Module:  budget_processor.py
Author:  Patrick Humphries
Orgainization:  USC Viterbi Analytics Bootcamp, 1/30
Input:  Type Boolean.  If True, budget model is written to screen and csv file.
Output:  Financial Analysis written to screen and text file.
Methods:  run(debug)
Description:
    1.  Read the input csv files.
    2.  Build a budget model with aggregated revenue by month.
    3.  Derive a sorted list of keys from the budget model.
    4.  Calculate aggregationn values by processing the budget model sequentially.
"""
import budget_factory
import os
import csv

def run(debug):
    # Select all csv files in the current directory to process.
    # Assumption:  csv file names start with "budget_data_"
    file_names = []
    directory_entries = os.listdir()
    for directory_entry in directory_entries:
        if directory_entry.startswith("budget_data_"):
            if directory_entry.endswith(".csv"):
                file_names.append(directory_entry)

    # Get the budget model created from the input csv files.
    budget_model = budget_factory.get_budget_model(file_names)

    # Write financial analysis to the screen and text file using the data model as the source.
    with open("financial_analysis.txt", "w") as report_file:
    
        report_line ="Financial Analysis"
        print(report_line)
        report_file.write(report_line)

        report_line = "\n-------------------------------"
        print(report_line)
        report_file.write(report_line)

        report_line = "\nTotal Months:  {}".format(budget_model["total_number_of_months"])
        print(report_line)
        report_file.write(report_line)

        report_line = "\nTotal Revenue:  ${:,.0f}".format(budget_model["total_revenue"])
        print(report_line)
        report_file.write(report_line)

        report_line = "\nAverage Revenue Change: ${:,.0f}".format(budget_model["average_revenue_change"])
        print(report_line)
        report_file.write(report_line)

        period = budget_model["greatest_increase"]
        report_line = "\nGreatest Increase in Revenue: {} (${:,.0f})".format( period["name"], period["revenue"])
        print(report_line)
        report_file.write(report_line)

        period = budget_model["greatest_decrease"]
        report_line = "\nGreatest Decrease in Revenue: {} (${:,.0f})".format( period["name"], period["revenue"])
        print(report_line)
        report_file.write(report_line)

    # If debug is True, write the budget model to the screen and csv file.
    if debug:
        with open("financial_analysis.csv", 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            print("\n")
            periods = budget_model["periods"]
            period_key_set = periods.keys()
            period_key_list = list(period_key_set)
            period_key_list.sort()
            for period_key in period_key_list:
                period = periods[period_key]
                print( "{} {} ${:,.0f}".format(period_key, period["name"], period["revenue"]))
                csv_writer.writerow([period_key, period["name"], period["revenue"]])

    input("Press Enter to continue.")
=======
"""
Module:  budget_processor.py
Author:  Patrick Humphries
Orgainization:  USC Viterbi Analytics Bootcamp, 1/30
Input:  Type Boolean.  If True, budget model is written to screen and csv file.
Output:  Financial Analysis written to screen and text file.
Methods:  run(debug)
Description:
    1.  Read the input csv files.
    2.  Build a budget model with aggregated revenue by month.
    3.  Derive a sorted list of keys from the budget model.
    4.  Calculate aggregationn values by processing the budget model sequentially.
"""
import budget_factory
import os
import csv

def run(debug):
    # Select all csv files in the current directory to process.
    # Assumption:  csv file names start with "budget_data_"
    file_names = []
    directory_entries = os.listdir()
    for directory_entry in directory_entries:
        if directory_entry.startswith("budget_data_"):
            if directory_entry.endswith(".csv"):
                file_names.append(directory_entry)

    # Get the budget model created from the input csv files.
    budget_model = budget_factory.get_budget_model(file_names)

    # Write financial analysis to the screen and text file using the data model as the source.
    with open("financial_analysis.txt", "w") as report_file:
    
        report_line ="Financial Analysis"
        print(report_line)
        report_file.write(report_line)

        report_line = "\n-------------------------------"
        print(report_line)
        report_file.write(report_line)

        report_line = "\nTotal Months:  {}".format(budget_model["total_number_of_months"])
        print(report_line)
        report_file.write(report_line)

        report_line = "\nTotal Revenue:  ${:,.0f}".format(budget_model["total_revenue"])
        print(report_line)
        report_file.write(report_line)

        report_line = "\nAverage Revenue Change: ${:,.0f}".format(budget_model["average_revenue_change"])
        print(report_line)
        report_file.write(report_line)

        period = budget_model["greatest_increase"]
        report_line = "\nGreatest Increase in Revenue: {} (${:,.0f})".format( period["name"], period["revenue"])
        print(report_line)
        report_file.write(report_line)

        period = budget_model["greatest_decrease"]
        report_line = "\nGreatest Decrease in Revenue: {} (${:,.0f})".format( period["name"], period["revenue"])
        print(report_line)
        report_file.write(report_line)

    # If debug is True, write the budget model to the screen and csv file.
    if debug:
        with open("financial_analysis.csv", 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            print("\n")
            periods = budget_model["periods"]
            period_key_set = periods.keys()
            period_key_list = list(period_key_set)
            period_key_list.sort()
            for period_key in period_key_list:
                period = periods[period_key]
                print( "{} {} ${:,.0f}".format(period_key, period["name"], period["revenue"]))
                csv_writer.writerow([period_key, period["name"], period["revenue"]])

    input("Press Enter to continue.")
>>>>>>> a46ccf54e7cdc6f82cafbdeccdfc490c67d6f4a7
