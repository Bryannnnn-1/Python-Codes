#This encryption will reverse the alphabet
#So if letter is A, the encrypted letter will be Z, B = Y, C = X, etc.
#Example, if u input "HELLO", It will be encrypted as "SVOOL"
#Check it out now!


import time

alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

reverseAlpha = ["Z","Y","X","W","V","U","T","S","R","Q","P","O","N","M","L","K","J","I","H","G","F","E","D","C","B","A"]


def getUserInput():
    bryan = True

    while bryan:

        print("Enter an decrypted Message to be encrypted")

        message = input(">>>>> ").upper().strip()


        if message == "":
            print("Do not leave any blank space!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(" ")
            bryan = True
        elif not (words.isalpha() or not words.isspace() for words in message):
            print("The encrypted message cannot contain numbers!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(" ")
            bryan = True
        else:
            return message
        


def encryption(message):
    encryptedMessage = ""

    for words in message:
        if words in alphabet:
            IndexOfLetter = alphabet.index(words)
            encryptedMessage += reverseAlpha[IndexOfLetter]
        else:
            encryptedMessage += words
            
    return encryptedMessage



def main():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Welcome to my Encryptor~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    print("~~~~~~~~~~~~~This program can decrypt letters....the numbers remain constant!~~~~~~~~~~~~~~~")
    print(" ")
    print("The numbers will remain the same!")
    print(" ")
    message = getUserInput()
    decryptedMessage = encryption(message)
    print("The Decrypted message is: ")
    print(f"{message}")
    print(" ")
    print("The Encrypted message is: ")
    print(" ")
    time.sleep(1)
    print("Hold on...")
    print(" ")
    time.sleep(1)
    print("Cracking code...")
    print(" ")
    time.sleep(1)
    print(f"'{decryptedMessage}' ")


main()