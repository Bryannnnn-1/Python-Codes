#Problem statement:  to write a program that will help its staff calculate the cost of buying smartphones for a business.
#by Bryan
#created on 16th december 2024
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#

def getCustomerInputData():#defining function to get input data 
    global customerName, address, phoneNumber
    while True:#loop to get input data
        customerName = input("Enter the Customer name: ").strip()#prompt the user to enter 
        print(" ")

        if not customerName:#making sure that the user inputs something
            print("No blank space!")
            print("***************************")
            continue
        elif not customerName.isalpha():#making sure that the user input is alphabet
            print("Enter a name not digit!")
            continue
        else:
            break#break out of the loop if the condition is true

    while True:#loop to get input data
        address = input("Enter the customer address: ").strip()#prompt the user to enter 
        print(" ")
         
        if not address:#making sure that the user inputs something
            print("No blank space!")
            print("********************************")
            continue
        else:
            break#break out of the loop if the condition is true

    while True:#loop to get input data
        phoneNumber = input("Enter the Customer phone number: ").strip()#prompt the user to enter 
        print(" ")
         

        if not phoneNumber:#making sure that the user inputs something
            print("No blank space!")
            print("**********************************")
            continue
        elif not phoneNumber.isdigit():#making sure that the user input a digit
            print("Phone number cannot be a letter! \n Retry!")
            print("***************************************")
            continue
        elif len (phoneNumber) != 10:#checking the length of the phone number
            print("please enter in 11 digits format\nRemove the leading zero(0)!")
            print("****************************")
            continue
        else:
            break#break out of the loop if the condition is true

def getCompanyDetails():#defining function to get input data 
    global companyName, companyPhoneNumber
    while True:#loop to get input data
        companyName = input("Enter the Company name: ").strip()#prompt the user to enter 
        print(" ")

        if not companyName:#making sure that the user inputs something
            print("No blank space!")
            print("********************")
            continue
        elif not companyName.isalpha():#making sure that the user input is alphabet
            print("Company name must be only letters!")
            print("*******************************")
        else:
            break#break out of the loop if the condition is true

    while True:#loop to get input data
        companyPhoneNumber = input("Enter the Company phone number: ").strip()#prompt the user to enter 
        print(" ")

        if not companyPhoneNumber:#making sure that the user inputs something
            print("No blank space!")
            print("**************************")
            continue
        elif not companyPhoneNumber.isdigit():#making sure that the user input is digit
            print("Phone number cannot be a letter! \nRetry!")
            print("**************************************")
            continue
        elif len (companyPhoneNumber) != 10:#checking the length of the phone number
            print("please enter in 11 digits format\nRemove the leading zero(0)!")
            print("***************************")
            continue
        else:
            break#break out of the loop if the condition is true

def getQuantityOfSmartPhone():#defining function to get input data 
    global quantityOfPhone
    while True:#loop to get input data
        print("The Minimum quantity of phone is 5!")
        print("The Maximum quantity of phone is 100!")
        print("The Quantity must be a multiple of 5")
        print("*********************************")

        try:
            quantityOfPhone = input("How many smartphones did the company buy: ")#prompt the user to enter 
            print(" ")

            if not quantityOfPhone:#making sure that the user inputs something
                print("No blank spaces please!")
                print("*****************************")
                continue
            else:
                quantityOfPhone = int(quantityOfPhone) 
                if (quantityOfPhone % 5 != 0):#ckeck if the user enters a multiple of 5
                    print("Please enter a multiple of 5, e.g, 5, 10, 15, 20,...........up to 100!")
                    print("*******************************************************")
                    continue
                elif quantityOfPhone <= 4 or quantityOfPhone >= 101:#check if the user enter a valid number
                    print("Please enter a multiple of 5. Not below 5/Not above 100!")
                    print("*************************************************")
                    continue
                else:
                    return quantityOfPhone
        except ValueError:
            print("Please Try Again!")
            

def getPhoneType():#defining function to get input data 
    global quantityOfPhone, phoneType, cost
    while True:#loop to get input data
        print("******************************************")
        print("SMARTPHONE TYPES AND PRICE PER PHONE ")
        print("1. Basic - £250")                                                            #smartphone types
        print("2. Standard - £450")
        print("3. Superior - £950")
        print(" ")

        phoneType = input("Choose from 1 - 3!\nWhat phone type did the company buy: ").strip()#prompt the user to enter 
        print(" ")

        if not phoneType:#making sure that the user inputs something
            print("No blank spaces!")
            print("********************************")
            continue
        else:
            try:
                phoneType = int(phoneType)#converting user input
                if phoneType == 1:
                    cost = quantityOfPhone * 250
                elif phoneType == 2:
                    cost = quantityOfPhone * 450
                elif phoneType == 3:
                    cost = quantityOfPhone * 950
                else:
                    print("Please enter a number from 1,2, or 3!")
                    print("************************************")
                    continue
                return cost
            except ValueError:
                print("Please Try Again!")

def getCostOfSetup():#defining function to get input data 
    global setupOption, cost
    while True:#loop to get input data
        print("******************************************")
        print("**SETUP OPTIONS**")
        print(" 1. Option A - £30")
        print(" 2. Option B - £50")
        print(" ")

        setupOption = input("Choose from 1 or 2\nWhat setup option did the company buy: ").strip().lower()#prompt the user to enter 
        print(" ")
        
        if not setupOption:#making sure that the user inputs something
            print("No blank spaces!")
            print("********************************")
            continue
        else:
            try:
                setupOption = int(setupOption)#converting user input
                if setupOption == 1:
                    setupOption = cost * 30
                elif setupOption == 2:
                    setupOption = cost * 50
                else:
                    print("Please enter a number from 1 or 2!")
                    print("************************************")
                    continue
                return cost
            except ValueError:
                print("Please Try Again!")
def taxCalculator():#function to calculate tax
    global cost, tax, totalcost
    tax = cost * 0.10
    totalcost = cost + tax
    return totalcost
    
    
    
def main():#definig a main function
    print("*************************WELCOME***********************************")
    getCustomerInputData()
    getCompanyDetails()
    getQuantityOfSmartPhone()                 #
    getPhoneType()                                       # calling on all the function
    getCostOfSetup()                                #
    taxCalculator()
    print("************SUMMARY OF THE PURCHASE****************")
    print(f"The Customer name is: {customerName}")
    print(f"The Customer address is: {address}")
    print(f"The Customer phone number is: +44{phoneNumber}")                          #
    print(f"The Company name is: {companyName}")                                       #printing the details
    print(f"The Company phone number is: +44{companyPhoneNumber}")        #
    print(F"The Quantity Of Phone is: {quantityOfPhone} phones")
    print(f"The total cost is: £{cost}.00")
    print(f"The tax amount is: £{tax}")
    print(f"The total cost is: £{totalcost}")
    
    



main()
    
            
