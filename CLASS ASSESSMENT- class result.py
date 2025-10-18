#PROBLEM STATEMENT: PROGRAM THAT ALLOWS A TEACHER TO ENTER STUDENT NAME TEST SCORE TO CALCULATE RESULT
#18TH NOVEMBER 2024
#BY BRYAN

print("***********************************************")

#INPUT SECTION
def getInputData(): #DEFINING A FUNCTION TO GET INPUT DATA
    while True:

        numberOfStudents = input("Enter the Number of students in the class: ")
        try:
            numberOfStudents = int(numberOfStudents)
            if int(numberOfStudents) <= 0:
                raise ValueError("Invalid Input!  Number must be greater than 0!")#TO MAKE SURE THAT THE TEACHER ENTERS A VALID NUMBER
            else:
                return numberOfStudents
        except ValueError as e:
            print(f"{e}")
            

#PROCESS SECTION
def GetTheTestScores(numberOfStudents): #function to get the test score and evaluate
    counter = 1
    while counter <= numberOfStudents:
        testResult = float(input("Enter the test score: "))
        if testResult <= 0 or testResult >= 101:
            print("Enter a number from 1 to 100!")#checking if the teacher inputed a valid test score
            print("******************************")
            GetTheTestScores()
        else:
            studentName = str(input("Enter the student name: "))
            print("**************************************")
            if (testResult >= 80) and (testResult <= 100):
                print(studentName)
                print(testResult)
                print("Distinction!")
            elif (testResult >= 60) and (testResult <= 79):
                print(studentName)
                print(testResult)
                print("Merit!")
            elif (testResult >= 50) and (testResult <= 59):
                print(studentName)
                print(testResult)
                print("Pass!")
            else:
                print(studentName)
                print(testResult)
                print("Failed!")
        
        
        counter += 1
        



def main(): #defining a main function
    numberOfStudents = getInputData()
    GetTheTestScores(numberOfStudents)


    

main() #calling the main function

