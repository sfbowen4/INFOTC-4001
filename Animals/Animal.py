#Stephen Bowen 2020
import random

class Animal:
    def __init__(self, animal_type, name):
        self.__animal_type = animal_type
        self.__name = name
        Moods = {1: 'happy', 2: 'hungry', 3: 'sleepy'}
        self.__mood = Moods[random.randint(1,3)]
    
    def get_animal_type(self):
        return self.__animal_type

    def get_name(self):
        return self.__name

    def check_mood(self):
        return self.__mood