#Stephen Bowen 2020
import Animal

Farm = []

def NewAnimal():
    AnimalType = str(input("\nWhat type of animal would you like to create? "))
    Name = str(input("What is the animal’s name? "))

    return Animal.Animal(AnimalType, Name)

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