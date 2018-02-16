# # Udemy - Web Course Breakdown
# ## Instructions
# * Create a Python application that reads the data on Udemy Web Development offerings. 
# * Then store the contents of the Title, Price, Subscriber Count, Number of Reviews, and Course Length into Python Lists.
# * Then zip these lists together into a single tuple.
# * Finally, write the contents of your extracted data into a CSV. Make sure to include the titles of these columns in your csv.
# ## Notes:
# * As, with many datasets, the file does not include the header line. Use the below as a guide on the columns: "id,title,url,isPaid,price,numSubscribers,numReviews,numPublishedLectures,instructionalLevel,contentInfo,publishedTime"
# ## Bonus:
# * Find the percent of subscribers that have also left a review on the course. Include this in your final output.
# * Parse the string associated with course length, such that we store it as an integer instead of a string. (i.e. "4 hours" should be converted to 4).
# 1 4 5 6
# title, price, susbscribers , reviews
# zero based
import os
csvpath = os.path.join('Resources', 'WebDevelopment.csv')

import csv
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    titleList = []
    priceList = []
    susbscriberList = []
    reviewList = []
    

    #  Each row is read as a row
    i = 0
    for row in csvreader:
        titleList.append(row[1])
        priceList.append(row[4])
        susbscriberList.append(row[5])
        reviewList.append(row[6])
        if i > 10:
            break

    myTuple = zip(titleList,priceList,susbscriberList,reviewList)
