#Stephen Bowen 2020
import string

asciiString = string.ascii_lowercase
alternatives = ('0','1','2','3','4','5','6','7','8','9','!','@','#','$','%','^','&','*','(',')','-','=','<','>','?','=')
masterCipher = {asciiString[i] : alternatives[i] for i in range(len(asciiString))}
inverseCipher = {y : x for x , y in masterCipher.items()}

def Encode():
    global masterCipher
    string = str(input("\nEnter a message to encode: "))
    result = ''
    for char in string:
        try:
            result += masterCipher[char]
        except:
            result += char
    
    print("Encoded message: {}\n".format(result))

def Decode():
    global inverseCipher
    string = str(input("\nEnter a message to encode: "))
    result = ''
    for char in string:
        try:
            result += inverseCipher[char]
        except:
            result += char
    
    print("Decoded message: {}\n".format(result))

def Main(selection):
    if selection == 1:
        Encode()
    elif selection == 2:
        Decode()
    elif selection == 3:
        return False

if __name__ == "__main__":
    loop = True
    while loop != False:
        print("Welcome to the Secret Message Encoder/Decoder\n1. Encode a message\n2. Decode a message\n3. Exit\n")
        while True:
            try:
                selection = int(input("What would you like to do? "))
            except ValueError:
                print("Please enter a number between 1 and 3")
            else:
                if 1 <= selection <= 3:
                    loop = Main(selection)
                    break
                else:
                    print("{} is not a valid selection. Please try again".format(selection))