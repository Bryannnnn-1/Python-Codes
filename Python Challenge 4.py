#problem statement: Write a program that takes an array of numbers as input and calculates the Mean, Median, Mode, Standard deviation.
#By Bryan
#24 feburary 2025

import array as arr
import statistics


num = arr.array('f',[])


def number():
    global length, digits
    bryan = True
    while bryan:
        print("How many digits do you want to enter?")
    
        userInput = input (">>>>>> ").strip()
        
        if not userInput:
            print("Do not leave any space blank!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(" ")
            bryan = True
        else:
            try:
                length = int(userInput)
            except ValueError:
                print("Invalid format!\nTry again!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" ")
                
            else:
                x = 1
                
                while x <= length:
                    digit = input("Enter digit - ").strip()
                    
                    if not digit:
                        print("Do not leave any space blank!")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print(" ")
                        haaland = True
                    else:
                        try:
                            digit = float(digit)
                            num.append(digit)
                            x += 1
                        except ValueError:
                            print("Invalid format!\nTry again!")
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print(" ")
                            
        print(num)
        bryan  = False
    
                        
                        
def mean():
    global length, digit
    
    mean = sum(num) / length
    
    print(f"The MEAN of the numbers is '{mean}'")

def median():
    for i in range(0, len(num)):
        for j in range(i+1, len(num)):
            if(num[i] > num[j]):
                temp = num[i];
                num[i] = num[j];
                num[j] = temp;
    
    
    middleNumber = statistics.median(num)
    print(f"The MEDIAN is '{middleNumber}'")
        

def mode():
    modeNumber = statistics.mode(num)
    print(f"The MODE is '{modeNumber}'")

def standardDeviation():
    stDev = statistics.stdev(num)
    print(f"The STANDARD DEVIATION is '{stDev}'")
    

def main():
    number()
    print(" ")
    mean()
    print(" ")
    median()
    print(" ")
    mode()
    print(" ")
    standardDeviation()
    print(" ")
    
main()

