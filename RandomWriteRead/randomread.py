#Stephen Bowen 2020

class ConvertedList:
    #Constructor
    def __init__(self, SourceFile):
        #Initialize MasterList and SourceFile
        self.MasterList = []
        self.SourceFile = SourceFile

        #Read in data from txt file
        try:
            with open(SourceFile, 'r') as data:
                for line in data.readlines():
                    self.MasterList.append(int(line))
        except FileNotFoundError:
            print("Could not find file!")
            self.MasterList = []

def Main(file):
    Data = ConvertedList(file)
    MasterList = Data.MasterList

    if MasterList == []:
        return "This list has no values! Please try again."
    
    print("List of random numbers in {}".format(Data.SourceFile))

    for i in MasterList:
        print(i)

    print("Random number count: {}".format(len(MasterList)))
    return ""

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
        print(Main('randomnum.txt'))
        GoAgain = Again()