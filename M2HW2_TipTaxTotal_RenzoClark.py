foodcost = float( input( "Please enter the charge of the food: " ) )
tip = 0.18 * foodcost
salesTax = 0.07 * foodcost
totalCost = foodcost + tip + salesTax
print( "Food Charge: $" + format( foodcost, ",.2f"), "Tip: $" + \
       format( tip, ",.2f" ), "Sales Tax: $" + format( salesTax, ",.2f"), \
       "totalCost: $" + format( totalCost, ",.2f"), sep = "\n")


        
