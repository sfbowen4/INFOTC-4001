#Stephen Bowen 2020
import time

class Tweet:

    def __init__(self, author, text, age=time.time()):
        self.__author = author
        self.__text = text
        self.__age = age

    def get_author(self):
        return self.__author

    def get_text(self):
        return self.__text

    def get_age(self):
        timeDelta = (time.time() - self.__age)

        if timeDelta < 60:
            return "{:.0f}s".format(timeDelta)
        elif 60 <= timeDelta < 3600:
            return "{:.0f}m".format(timeDelta / 60)
        elif 3600 <= timeDelta:
            return "{:.0f}h".format(timeDelta / 3600)
        else:
            return "Could not determine age."
