#M6T1-Kilometer Converter
#CTI-110
#Renzo Clark
#Oct. 30, 2017

def askUserForKilometers():
    Kilometers = float( input("Enter distance " +\
                              "in kilometers: "))
    return Kilometers

def convertKilometersToMiles( Kilometers ):
    miles = Kilometers * 0.6214
    return miles

def main():
    Kilometers = askUserForKilometers()
    convertedMiles = convertKilometersToMiles( Kilometers )

    print( "\n", Kilometers, "Kilometers =", \
           format( convertedMiles, ".2f" ), " miles", sep="")
main()    
