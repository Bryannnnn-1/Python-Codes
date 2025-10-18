#refined
#This code will allow the user to enter numbers in unsorted order,
#then it will be sorted using bubble sort algorithm.

import array as arr

numArray = arr.array("i", [])#Creating an empty array

def getInputData():#defining a function to get input data
    length = int(input("How many number do you want to check: "))#getting the length of number
    x = 1 #initialise
    
    while x <= length:#A loop to get the digits to be sorted
        digits = int(input("Enter Digit - "))
        x = x+1
        numArray.append(digits)#assigning the digits to the empty array
    return length

def BubbleSort(length):
    print("The Unsorted Array is:")
    print(numArray)#display the unsorted array
    
    exchangeMade = True
    length = length - 1
    
    while exchangeMade:
        exchangeMade = False
        for k in range(length):
            if numArray[k] > numArray[k + 1]:
                #Exchange array elements
                
                temp = numArray[k]
                numArray[k] = numArray[k + 1]
                numArray[k + 1] = temp 
                exchangeMade = True
                
                
def main():#creating a main fuction
    length = getInputData()
    BubbleSort(length)
    print("The Sorted Array is: ")
    print(numArray)#display the sorted array
    

main()