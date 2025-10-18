#refined
#When I was still a newbie :)
print("******************************************")
print("******************************************")

def getInputData():
    global month, year, totalAmountCollected, countySalesTax
    month = str(input("Enter the month: "))
    year = int(input("Enter the year: ")) #collecting input data from client
    totalAmountCollected = float(input("Enter the total amount collected at the cash register: £"))


def calculator():
    global salesTaxAmount, S, countySalesTax, stateSalesTax #declare local variable  
    salesTaxAmount = totalAmountCollected * 0.06 #calculation
    S = totalAmountCollected - salesTaxAmount #calculation
    countySalesTax = S * 0.02 #calculation
    stateSalesTax = S * 0.04 #calculation

def main():
    getInputData()
    calculator()
    print("The month is: ", month)
    print("The year is: ", year)
    print("The total amount collected at the cash register is: £", totalAmountCollected)
    print("S is.........: £", S)
    print("County sales tax is: £", countySalesTax)
    print("Your states sales tax is: £", stateSalesTax)  


main()  #calling on the main function
