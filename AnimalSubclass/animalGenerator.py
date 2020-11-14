#Stephen Bowen 2020
import Animal

Farm = []

def NewAnimal():
    Animals = {1: 'mammal', 2: 'bird'}
    print("Would you like to create a mammal or bird?\n1. Mammal\n2. Bird")
    UserSelection = int(input("Which would you like to create? "))

    if UserSelection == 1:
        AnimalType = str(input("\nWhat type of {} would you like to create? ".format(Animals[UserSelection])))
        Name = str(input("What is the {}'s name? ".format(Animals[UserSelection])))
        Hair = str(input("What color is the {}'s hair? ".format(Animals[UserSelection])))
        return Animal.Mammal(AnimalType, Name, Hair)

    elif UserSelection == 2:
        AnimalType = str(input("\nWhat type of {} would you like to create? ".format(Animals[UserSelection])))
        Name = str(input("What is the {}'s name? ".format(Animals[UserSelection])))
        Fly = str(input("Can the {} fly? ".format(Animals[UserSelection])))
        return Animal.Bird(AnimalType, Name, Fly)

    else:
        print("Please choose either 1 or 2\n")
        NewAnimal()


print("Welcome to the animal generator!\nThis program creates Animal objects.")
while True:
    Farm.append(NewAnimal())
    User = input("\nWould you like to add more animals? (y/n) ")
    User = User.lower()
    if User == "y":
        None
    else:
        break

print("\nAnimal List:")
for animal in Farm:
    print("{} the {} is {}.".format(animal.get_name(), animal.get_animal_type(), animal.check_mood()))