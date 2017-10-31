#M6T2-Feet to Inches
#CTI-110
#Renzo Clark
#Oct. 30, 2017

def feetToinches(userFeet):
    inches=(userFeet/1)*12
    return inches
def main():
    userFeet=float(input("Enter number of feet:"))
    print()
    inches=feetToinches(userFeet)
    print(userFeet,"Feet to inches is",format(inches,".2f"),"inches")
main()    
