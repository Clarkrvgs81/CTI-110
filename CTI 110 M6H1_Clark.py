# Creating a Test Averaging Program
# Oct. 30 2017
# CTI-110 M6HW1 - Test Average and Grade
# Renzo Clark

def calc_average(Grade1, Grade2, Grade3, Grade4, Grade5):
    average=(Grade1, Grade2, Grade3, Grade4, Grade5)/5
    return average
def determine_grade(userGrade):
    if(userGrade<60):
        return"F"
    elif(userGrade<70):
        return"D"
    elif(userGrade<80):
        return"C"
    elif(userGrade<90):
        return"B"
    elif(userGrade<101):
        return"A"
def askForGrades():
    Grade1=float(input("Enter Grade 1:"))
    Grade2=float(input("Enter Grade 2:"))
    Grade3=float(input("Enter Grade 3:"))
    Grade4=float(input("Enter Grade 4:"))
    Grade5=float(input("Enter Grade 5:"))
    return Grade1, Grade2, Grade3, Grade4, Grade5
def printResults(Grade1, Grade2, Grade3, Grade4, Grade5):
    print(str(Grade1)+"\t\t"+determine_grade(Grade1),\
          str(Grade2)+"\t\t"+determine_grade(Grade2),\
          str(Grade3)+"\t\t"+determine_grade(Grade3),\
          str(Grade4)+"\t\t"+determine_grade(Grade4),\
          str(Grade5)+"\t\t"+determine_grade(Grade5),sep="\n")
def main():
    Grade1, Grade2, Grade3, Grade4, Grade5=askForGrades()
    print()
    printResults(Grade1, Grade2, Grade3, Grade4, Grade5)
main()


