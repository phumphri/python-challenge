"""
Module:  budgetModel.py
Author:  Patrick Humphries
Organization:  USC Viterbi Analytics Boot Camp, January 30, 2018

Description:  Provide a budget model which provides aggregated values from
    multiple csv files.
    
Assumptions:
    1. Input files will be regular CSV files.
    2. First row will be a header.
    3. Columns are Date and Revenue.
Methods:
    get_budget_model(file_names)
"""
import csv
import datetime

def get_budget_model(file_names):
    """
    Module:  budget_factory
    Function:  get_budget_model
    Parameter:  File name of a CSV file with revenue data.
    Return:  Budget Model, type dict, containing aggregated revenue data.
    """
    # Define Budget Model
    # {
    #   "periods": periods,
    #   "total_number_of_months": total_number_of_months,
    #   "total_revenue": total_revenue
    # }
    budget_model = {}
    budget_model["total_number_of_months"] = 0
    budget_model["total_revenue"] = 0

    # Each period in periods contains aggregated information for that period.
    # {
    #   "period_key": period
    # }
    periods = {}
    budget_model["periods"] = periods

    # Each period has attributes.
    # {
    #   "name": period_name
    #   "revenue": revenue (aggregated)
    # }

    # Process each csv file found in the list argument.
    for file_name in file_names:
        try:
            # Process the csv file.
            with open(file_name, 'r', encoding='ascii') as csv_file:

                # Create a reader for the CSV file.
                csv_reader = csv.reader(csv_file, delimiter=',')

                process_rows(csv_reader, budget_model)

        except FileNotFoundError as error:
            print('\nIn budget_model.py a ' \
                    'FileNotFoundError was thrown for file {}.'.format(file_name))
            print('FileNotFoundError.args:')
            for arg in error.args:
                print('\t', arg)
            print('\n')
            exit(1)

        except IOError as error:
            print('\nIn budget_model.py a ' \
                    'IOError was thrown for file {}.'.format(file_name))
            print('FileNotFoundError.args:')
            for arg in error.args:
                print('\t', arg)
            print('\n')
            exit(1)

    # Sort and aggregate periods.
    sort_and_aggregate_periods(budget_model)

    # Return budgt model containing aggregated amounts.
    return budget_model

def process_rows(csv_reader, budget_model):
    """
    For each row in the csv_reader, either add or update the period in the budget model.
    From the date field, a period key is formatted.  The period key will be used for processing
    the budget model in chronological order.
    """
    # Metadata
    date_column = 0
    revenue_column = 1

    i = 0   # Unit Tesing

    for row in csv_reader:

        # Unit Testing
        # i = i + 1
        # if i > 4:
        #     break

        date_string = str(row[date_column])

        # Bypass header.
        if date_string == "Date":
            continue
    
        # Format period key.
        month_name = date_string[:3].lower()
        if month_name == "jan":
            period_month = "01"
        elif month_name == "feb":
            period_month = "02"
        elif month_name == "mar":
            period_month = "03"
        elif month_name == "apr":
            period_month = "04"
        elif month_name == "may":
            period_month = "05"
        elif month_name == "jun":
            period_month = "06"
        elif month_name == "jul":
            period_month = "07"
        elif month_name == "aug":
            period_month = "08"
        elif month_name == "sep":
            period_month = "09"
        elif month_name == "oct":
            period_month = "10"
        elif month_name == "nov":
            period_month = "11"
        elif month_name == "dec":
            period_month = "12"
        else:
            raise ValueError('Month String was invalid: ' + date_string)
        period_year = date_string[-2:]
        period_key = period_year + period_month

        # Format period name.
        period_name = month_name + "-" + period_year
        period_name = period_name.capitalize()

        # Get revenue.
        revenue = float(row[revenue_column])

        # If the period already exists, add the revenue to the period.
        # If the period does not exist, add the period with its revenue.
        periods = budget_model["periods"]

        if period_key in periods:
            period = periods[period_key]
            period["revenue"] = period["revenue"] + revenue
        else:
            period = {}
            period["name"] = period_name
            period["revenue"] = revenue
            periods[period_key] = period
    
def sort_and_aggregate_periods(budget_model):
    """
    Calculate aggregations by processing the budget model in chronological order.
    """
    # Calculate total number of months.
    periods = budget_model["periods"]      
    total_number_of_months = len(periods)    
    budget_model["total_number_of_months"] = total_number_of_months

    # Get the reference to the total revenue in the budget model.
    total_revenue = budget_model["total_revenue"]

    # Initialize variables used to calculate greatest increase in revenue.
    greatest_increase_revenue = 0
    greatest_increase_name = ""

    # Initialize variables used to calculate greatest decrease in revenue.
    greatest_decrease_revenue = 0
    greatest_decrease_name = ""

    # Retrieve sort keys for budget model and sort them into chronological order.
    period_keys = periods.keys()
    period_key_list = list(period_keys)
    period_key_list.sort()

    # Initialize previous revenue.
    # There is no revenue change for the first period.
    previous_revenue = periods[period_key_list[0]]["revenue"]
    total_revenue_change = 0

    # Calculate aggregations by processing periods in chronological order.
    for period_key in period_key_list:
        period = periods[period_key]
        total_revenue = total_revenue + period["revenue"]

        budget_model["total_revenue"] = total_revenue

        revenue = period["revenue"]
        revenue_change = revenue - previous_revenue
        total_revenue_change = total_revenue_change + revenue_change
        
        if revenue_change > greatest_increase_revenue:
            greatest_increase_revenue = revenue_change
            greatest_increase_name = period["name"]

        if revenue_change < greatest_decrease_revenue:
            greatest_decrease_revenue = revenue_change
            greatest_decrease_name = period["name"]

        previous_revenue = revenue

    # Write aggregations to the budget model.
    budget_model["greatest_increase"] = {"name": greatest_increase_name, "revenue": greatest_increase_revenue}
    budget_model["greatest_decrease"] = {"name": greatest_decrease_name, "revenue": greatest_decrease_revenue}
    budget_model["average_revenue_change"] = round(total_revenue_change / total_number_of_months, 0)
