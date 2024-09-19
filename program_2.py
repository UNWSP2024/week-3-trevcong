# AUTHOR: Trevor Conger UNWSP 
# DATE: 9/19/24 
# TITLE: If age > or < 

#PSEUDOCODE #1 AGE CLASSIFIER

#------------------------------------------------------------------#
# categorize_age function is called with PARAM ( age as a float )
# ageCategory var is set to a string "TBD"
# IF age <= 1
    # geCategory = "Infant"
# ELSE IF 1 < age < 13
    # geCategory = "Child"
# ELSE IF 13 <= age < 20
    # geCategory = "Teenager"
# ELSE IF age > 20 
    # geCategory = Adult"

# RETURN: Age as a string ( infant, child, teenager, adult )
#-------------------------------------------------------------------#


# PROGRAM #2 AGE CLASSIFIER

# This function takes in input as a float ( age ) to then decide what ageCategory they will be placed in
def categorize_age(age):
    ageCategory = "TBD"
    if age <= 1:
        ageCategory = "infant"
    elif age > 1 and age < 13:
        ageCategory = "child"
    elif age >= 13 and age < 20:
        ageCategory = "teenager"
    else:
        ageCategory = "adult"

    return ageCategory

if __name__ == '__main__':
    # Local variables
    # Get age from the user.
    age = float(input("Enter the person's age: "))
    # Display the age
    ageBucket = categorize_age(age)
    print (ageBucket)