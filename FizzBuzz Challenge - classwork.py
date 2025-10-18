#PROBLEM STATEMENT: a program that prints numbers from 1 to 50.  
#For multiples of 3, print "Fizz" instead of the number. 
#For multiples of 5, print "Buzz" instead of the number. 
#For multiples of both 3 and 5, print "FizzBuzz."

#By Bryan

def FizzBuzzPrinter():#defining the function
    for digits in range(1,51):#a loop to run digits from 1 to 50
        if digits % 3 == 0 and digits % 5 == 0:#checking if the digits is a multiple of 5 and 3
            print("'FizzBuzz'")
        elif digits % 3 == 0:#checking if the digits is a multiple of 3
            print("'Fizz'")
        elif digits % 5 == 0:#checking if the digits is a multiple of 5
            print("'Buzz'")
        else:#if not, print the digit 
            print(digits)#printing the digits.


FizzBuzzPrinter()#calling on the function


