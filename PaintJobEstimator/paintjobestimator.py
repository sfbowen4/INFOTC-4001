#Stephen Bowen 2020
import math

def InputVariable(variable, NegativeAllowed):
    while True:
        try:
            value = float(input(variable))
        except ValueError:
            print("Please only enter a number.")
        else:
            if NegativeAllowed == True:
                return value
            else:
                if value < 0:
                    print("Please only enter a number > 0.")
                elif value > 0:
                    return value

def Main():
    HourlyRate = 62.25
    Wall = InputVariable("How many square feet is the wall?\n", False)
    PaintPrice = InputVariable("How much does the paint cost per gallon?\n$", False)

    #Calculate paint needed (whole number)
    Paint = (1/350) * Wall
    Paint = math.ceil(Paint)
    print("{} gallon(s) of paint required.".format(Paint))

    #Calculate hours of labor (one decimal)
    Hours = (6/350) * Wall
    Hours = round(Hours, 1)
    print("{} hours of labor required.".format(Hours))

    #Calculate cost of paint on rounded gallons
    TotalPaintCost = Paint * PaintPrice
    TotalPaintCost = round(TotalPaintCost, 2)
    print("Paint cost: ${:.2f}".format(TotalPaintCost))

    #Calculate labor charges
    Labor = Hours * HourlyRate
    print("Labor cost: ${:.2f}".format(Labor))

    #Calculate total cost
    TotalCost = Labor + TotalPaintCost
    print("Total cost: ${:.2f}".format(TotalCost))

def Again():
    User = input("Would you like to do another estimate? (y/n)\n")
    User = User.lower()
    if User == "y":
        return True
    elif User == "n":
        return False
    else:
        Again()

if __name__ == "__main__":
    GoAgain = True
    while GoAgain == True:
        Main()
        GoAgain = Again()
