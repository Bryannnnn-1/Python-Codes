#Program statement: Getting input from user and storing them in a dictionary
#Created on 20 November, 2024
#by Bryan

print("Welcome to my program!")
print("********************************************************")

import array as arr #importing the array 

numArray = []#creating an empty array

StudentDetails = {}#creating an empty dictionary

def getInputData():#creating a function to get input data from user
    while True:
        userInput = input("How many entries do you want to make: ").strip()
       
        # Check if input is empty or invalid
        if not userInput:
            print("Please don't leave the space blank!")
            print("*****************************")
            continue
       
        try:
            Entry = int(userInput)
            if Entry <= 0:
                print("Please enter a number greater than 0.")
                print("************************************")
                continue
            else:
                break  # Valid number for entries, break the loop
               
        except ValueError:
            print("Please enter a valid number!")
            print("**********************************")




    # Loop to collect key-value pairs
    for i in range(Entry):   
        while True:
        # Get and validate the key
            Input = input("Enter the key: ").strip()
            
            if not Input.isalpha():  # Ensure the key contains only alphabets
                print("Key must contain alphabets only!")
                print("*****************************")
                continue
            elif not Input:  # Ensure the key is not empty
                print("Key cannot be empty!")
                print("*****************************")
                continue
            else:
                break  # Key is valid, exit loop


            # Ask for value only after key validation
        while True:
            InpuT = input("Enter the value (integer required): ").strip()
            
            if not InpuT:  # Ensure value is not empty
                print("Value cannot be empty!")
                print("*****************************")
                continue
            
            try:
                value = int(InpuT)  # Convert value to integer
                break  # Exit loop after valid value input
            except ValueError:
                print("Value must be an integer!")
                print("**********************************")

            # Add the valid key-value pair to the dictionary
        StudentDetails[Input] = value


# Call the function to execute
getInputData()
# Print the final dictionary
print("The dictionary you created is:", StudentDetails)