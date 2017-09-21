# CTI-110
# M3HW1 - Age Classifier
# Renzo Clark
# 9/12/17
#

def main():

    # This program identifies age groups
    
    Infant = 1
    Child = 13
    Teenager = 20


    Age = int(input('Enter age: '))
    if Age <= Infant:
      print ('Person is an: Infant.')
    elif Age < Child:
      print ('Person is a: Child.')
    elif Age < Teenager:
      print ('Person is a: Teenager.')
    else: 
      print ('Person is an: Adult.')

main()      

    
