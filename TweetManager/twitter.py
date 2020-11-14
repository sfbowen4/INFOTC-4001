#Stephen Bowen 2020
import pickle
from Tweet import Tweet

twitterFeed = []

#Tweet
def makeTweet():
    global twitterFeed
    author = str(input("\nWhat is your name? "))
    text = str(input("What would you like to tweet? "))

    while len(text) > 140:
        print("Tweets can only be 140 characters!")
        text = str(input("What would you like to tweet? "))
    
    else:
        twitterFeed.append(Tweet(author, text))
        saveTweets()
        loadTweets()
        print("{}, your tweet has been saved.".format(author.capitalize()))

#View tweets
def viewRecent():
    global twitterFeed

    print("\nRecent Tweets\n-——————")

    for i in range(4 if len(twitterFeed) > 4 else len(twitterFeed)):
        i = -(i + 1)
        tweet = twitterFeed[i]
        print("{} - {}".format(tweet.get_author(),tweet.get_age()))
        print("{}\n".format(tweet.get_text()))

#Search for text within tweets
def searchTweets():
    global twitterFeed
    searchParam = str(input("\nWhat would you like to search for? "))
    emptySearch = True

    print("\nSearch Results\n-——————")
    for tweet in twitterFeed:
        if searchParam in tweet.get_text():
            print("{} - {}".format(tweet.get_author(),tweet.get_age()))
            print("{}\n".format(tweet.get_text()))
            emptySearch = False
        else:
            pass
    if emptySearch == True:
        print("No tweets contain {}.".format(searchParam))

#Save tweets to pickle file in the same directory
def saveTweets():
    global twitterFeed

    twitterArchive = open("twitterArchive.pickle", "wb")
    pickle.dump(twitterFeed, twitterArchive)
    twitterArchive.close()
    twitterFeed = []

#Load archived tweets from pickle file in the same directory
def loadTweets():
    global twitterFeed

    twitterArchive = open("twitterArchive.pickle", "rb")
    twitterFeed = pickle.load(twitterArchive)
    twitterArchive.close()

#Check for bad inputs
def Choice():
    while True:
        try:
            value = int(input("\nWhat would you like to do? "))
        except ValueError:
            print("Please only enter a number.")
        else:
            if 0 < value < 5:
                return value
            else:
                print("Please enter a valid option.")

#Menu and choice logic
def Twitter():
    print("\nTweet Menu\n-—————")
    print("1. Make a Tweet")
    print("2. View Recent Tweets")
    print("3. Search Tweets")
    print("4. Quit")
    choice = Choice()
    if choice == 1:
        makeTweet()
        return True
    elif choice == 2:
        viewRecent()
        return True
    elif choice == 3:
        searchTweets()
        return True
    else:
        return False

#Main loop
twitterOn = True
loadTweets()
while twitterOn:
    twitterOn = Twitter()
else:
    print("\nThank you for using the Tweet Manager!")