#Stephen Bowen 2020

#Input function
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
                    print("Please only enter a number >= 0.")
                elif value >= 0:
                    return value

#Calculate final position
def ObjectPosition():
    #Check and assign variables to input
    x_0 = InputVariable("Initial Position: ", True)
    v_0 = InputVariable("Initial Velocity: ", True)
    a = InputVariable("Acceleration: ", True)
    t = InputVariable("Time: ", False)

    #Calculate final position
    x_f = x_0 + (v_0 * t) + (.5 * a * (t ** 2))

    #Print final position
    print("The final position is {} units".format(x_f))

    #Go Again
    GoAgain = str(input("Calculate another object's position? (Y/N): "))
    if GoAgain.lower() == "y":
        ObjectPosition()
    else:
        print("Have a nice day!")
        
#Main
if __name__ == "__main__":
    ObjectPosition()

