# The list of candies to print to the screen
candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", \
"Sweedish Fish", "Skittles", "Hershey Bar", "Skittles", "Starbursts", "M&Ms"]

# The amount of candy the user will be allowed to choose
allowance = 5
# The list used to store all of the candies selected inside of
candyCart = []
for i in range(allowance):
    candyCart.append(candyList.pop())
for candy in candyCart:
    print(candy)
