import time


def slow(word):
    for char in word:
        print(char, end='', flush = True)
        time.sleep(0.03)
slow("This program will take a user input and display the division table for the number from 1 - 50")
print()
print()
def getUserInput():
    while True:
        slow("which number do you want to see it's division table? ")
        print()

        try:
            num = int(input(">>>>> "))
            if num < 1:
                raise ValueError
            else:
                return num
        except ValueError:
            print("Zero is not allowed and the number must be an integer❗")

def logic(num):
    print()
    print()
    print(f"Division table for {num}")
    print()

    for digit in range(1, 51):
        print(f"{num}  /  {digit}  =  {num / digit}")


num = getUserInput()
logic(num)
