# AUTHOR: Trevor Conger UNWSP 
# DATE: 9/19/24 
# TITLE: Hot dog or chili dog ?! 




# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost. 


#Function to take someones order as either a hot dog or chili dog 
# Asks user if they want toppings ( they are extra $ )
# Returns to user the TOTAL COST , TAX , TOTAL COST + TAX 
def orderFunction():
    ordercostTaxAndTotalCost = []
    print("Hello and welcome to Trevors Hot Dogs! \n")
    print("MENU")
    print("COMBO 1 : HOT DOG__________________$3.50")
    print("COMBO 2 : CHILI DOG________________$4.50")
    valueForTrue = True
    while(valueForTrue):
        try:
            userSelectionForHotDog = int(input("So what would you like? Combo 1 or 2?"))
            if userSelectionForHotDog == 1:
                ordercostTaxAndTotalCost.append(3.50) 
                print("Great choice! Can't go wrong with a plain dog while watching the Twin's play! \n")
                doYouWantCheese = input("Do you want cheese on your hot dog? (yes or no) \n").lower().strip()
                if doYouWantCheese == "yes":
                    ordercostTaxAndTotalCost[0] = ordercostTaxAndTotalCost[0] + .50
                doYouWantPeppers = input("Do you want peppers on your hot dog? (yes or no) \n").lower().strip()
                if doYouWantPeppers == "yes":
                    ordercostTaxAndTotalCost[0] = ordercostTaxAndTotalCost[0] + .75
                doYouWantGrilledOnions = input("Do you want peppers on your hot dog? (yes or no) \n")
                if doYouWantGrilledOnions == "yes":
                    ordercostTaxAndTotalCost[0] = ordercostTaxAndTotalCost[0] + 1.00
                ordercostTaxAndTotalCost.append((ordercostTaxAndTotalCost[0] * 0.07))
                ordercostTaxAndTotalCost.append(ordercostTaxAndTotalCost[0] + ordercostTaxAndTotalCost[1])
                break
                
            if userSelectionForHotDog == 2:
                ordercostTaxAndTotalCost.append(4.50)
                print("Great choice! Can't go wrong with a chili dog while watching the Twin's play! \n")
                doYouWantCheese = input("Do you want cheese on your chili dog? (yes or no) \n").lower().strip()
                if doYouWantCheese == "yes":
                    ordercostTaxAndTotalCost[0] = ordercostTaxAndTotalCost[0] + .50
                doYouWantPeppers = input("Do you want peppers on your chili dog? (yes or no) \n").lower().strip()
                if doYouWantPeppers == "yes":
                    ordercostTaxAndTotalCost[0] = ordercostTaxAndTotalCost[0] + .75
                doYouWantGrilledOnions = input("Do you want peppers on your chili dog? (yes or no) \n")
                if doYouWantGrilledOnions == "yes":
                    ordercostTaxAndTotalCost[0] = ordercostTaxAndTotalCost[0] + 1.00
                ordercostTaxAndTotalCost.append((ordercostTaxAndTotalCost[0] * 0.07))
                ordercostTaxAndTotalCost.append(ordercostTaxAndTotalCost[0] + ordercostTaxAndTotalCost[1])
                break
            else:
                continue
        except ValueError:
            print("Thats not a selection..")

    return ordercostTaxAndTotalCost


if __name__ == '__main__':
    order = orderFunction()
    print("Your hot dog will cost you $" + str(order[0]))
    print("Your tax will be $" + str(order[1]))
    print("Your final cost will come to $ " + str(order[2]))
