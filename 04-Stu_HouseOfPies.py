# Create an order form that will display a list of pies to the user in the following way:


# Welcome to the House of Pies! Here are our pies:

# ---------------------------------------------------------------------
# (1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee,  (5) Black Bun, (6) Blueberry, 
# (7) Buko, (8) Burek,  (9) Tamale, (10) Steak

# Then prompt the user to select which pie they'd like to order via number.
# Immediately after, follow the order with Great! We'll have that <PIE NAME> right out for you. and then ask if they would like to make another order. If so, repeat the process.
# Once the user is done purchasing pies, print the total number of pies ordered.

pies = []
pies.append("Pecan")
pies.append("Apple Crisp")
pies.append("Bean")
pies.append("Black Bun")
pies.append("Blueberry")
pies.append("Buko")
pies.append("Burek")
pies.append("Tamale")
pies.append("Steak")

piesPurchased = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

i = 1
print("Welcome to the House of Pies!  Here are our pies:")
textString = ""
for pie in pies:
    textString = textString + "(" + str(i) + ") " + pie + "  "
    i += 1
print(textString)
userSelection = "y"
while userSelection == "y":
    intSelection = int(input("\nWhich pie do you want?  "))
    print("Here's your " + pies[intSelection - 1] + " pie.")
    piesPurchased[intSelection - 1] =+ 1
    userSelection = input("Do you want another?  ")

for pie in pies:
    print(pie + ": ", piesPurchased[pies.index(pie)])
