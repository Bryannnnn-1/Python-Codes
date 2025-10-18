#refined
#PROBLEM STATEMENT: A program that takes an array of integers and finds the second largest numberin the array
#BY BRYAN

import time

import array as arr#importing the array function

myArray = arr.array('i',[])#creating an empty array

def getRequiredData(): #defining a function
    while True:#loop to get input data
        userInput = input("how many numbers do you want to store: ").strip()#get input data

        if not userInput:#presence check
            print("No blank spaces please!")#error message
            print(" ")
            continue#gives the user chance to try again
        else:
            try:#try converting to integer
                length = int(userInput)
                break#break out of the loop
            except ValueError:#except
                print("This is not a valid digit...please try again!")#error message

    return length
            


def getAndStoreDigits(length):#function to get and store the digits 
    x = 1#initialise a counter
    
    while x <= length:#looooop
        while True:#infinite loop
            UserInput = input("Enter digit - ")#get the digits

            if not UserInput:#presence check
                print("Do not leave any blank space!")#error message
                print(" ")
                continue#gives the user chance to try again
            else:
                try:#try converting the digit to integer
                    digits = int(UserInput)
                    myArray.append(digits)#append the input to the end of the list
                    x += 1#counter  
                    break
                except ValueError:#except
                    print("Please, enter a digit!")#error message

def sortTheArray(length):#function to sort the array
    # sorting the array using a selection sort
    for x in range(length):
        temp = myArray[x]
        index = x

        for y in range(x + 1, length):
            if myArray[y] < temp:
                temp = myArray[y]
                index = y

        myArray[index] = myArray[x]
        myArray[x] = temp
        secondLargest = myArray[-2]
        #finishing the sort. it is sorted in ascending order
    return secondLargest

def secondLargestNumberFinder(secondLargest):#function to get the second largest

    #returning the second largest of the array

    print("The numbers you inputted are: ")#printing the array
   
    print(myArray)

    print(f"The second largest number is: {secondLargest} ")#displaying the second largest
 

def main():#defining a main function to run the code
    length = getRequiredData()#calling function
    getAndStoreDigits(length)#calling function
    secondLargest = sortTheArray(length)#calling function
    secondLargestNumberFinder(secondLargest)#calling function


main()#calling the main function