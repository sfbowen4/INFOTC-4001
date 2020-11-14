#Stephen Bowen 2020

#Convert SourceFile to iterable list of integers
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

#Sum of integers in list
def Sum(Data):
    Total = 0
    for number in Data:
        Total += number
    
    return Total

#Count number of integers in list
def Count(Data):
    return len(Data)

#Average the integers in list
def Average(Data):
    return Sum(Data) / Count(Data)

#Largest number in list
def Maximum(Data):
    return max(Data)

#Smallest number in list
def Minimum(Data):
    return min(Data)

def Range(Data):
    return max(Data) - min(Data)
    
#Main function to take user input and create output
def Main(file):
    Data = ConvertedList(file)
    MasterList = Data.MasterList

    if MasterList == []:
        return "This list has no values! Please try again."
    
    print(Data.SourceFile)
    print(Sum(MasterList))
    print(Count(MasterList))
    print(Average(MasterList))
    print(Maximum(MasterList))
    print(Minimum(MasterList))
    print(Range(MasterList))

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
        print(Main(str(input('Enter a file name: '))))
        GoAgain = Again()