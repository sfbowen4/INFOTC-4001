#Stephen Bowen 2020
import random

def InputVariable(variable, NegativeAllowed):
    while True:
        try:
            value = int(input(variable))
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

def RandomWrite():
    Quantity = InputVariable('How many random numbers do you want? ', False)
    Lower = InputVariable('What is the lowest the random number should be? ', False)
    Upper = InputVariable('What is the highest the random number should be? ', False)

    while Lower >= Upper:
        print("The lowest number cannot be equal to or larger than the highest number!")
        Upper = InputVariable('What is the highest the random number should be? ', False)

    with open ("randomnum.txt", 'w') as WriteFile:
        for i in range(Quantity):
            WriteFile.writelines("{}\n".format(random.randint(Lower, Upper)))

    print("Random numbers written to 'randomnum.txt'")

def Again():
    User = input("Would you like to write another set of random numbers? (y/n)\n")
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
        RandomWrite()
        GoAgain = Again()