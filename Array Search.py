#Problem statement:  to write a program that will search for a specific value in a array and output its index
#by Bryan
#created on 02nd december 2024
#************************************************************************************************#

import array as arr#importing the array#listing the array containing only integers

def getInputToSearchFor():#creating function to get input data
    while True:#loop to get input data
        print("Which number do you want to search for?")
        userInput = input(">>>> ")#get input data

        if not userInput:#presence check
            print("Don,t leave the space blank!")
            print("*****************************************************************")
            print(" ")
            continue#give the user chance to enter again
        else:
            try:#try converting the input to integer
                if int(userInput) == False:
                    continue
                else:
                    number = userInput
                return number
            except ValueError:#if it cannot be converted to integer
                print("This input is not valid!")
                print("************************************************************")
                print(" ")
    

def main():#defining a main function to run the code
    ListOfNumbers= arr.array('i',[10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    print("*************W*E*L*C*O*M*E***T*O***M*Y***P*R*O*G*R*A*M*!***************")
    print(" ")
    number = getInputToSearchFor()#calling function
    print(f"The number you inputted is '{number}' ")
    print(" ")
    if number in ListOfNumbers:#checking if the number is in the array
        print(f"...And, the Value '{number}' is found at index {ListOfNumbers.index(number)} of the Array!")
    else:#if not, print value not found
        print(f"...Opss! the Value '{number}' not Found!")
    print(" ")
    print("************E*N*D***O*F***M*Y***P*R*O*G*R*A*M*!*****************")


main()##calling the main fuction for the code to be executed