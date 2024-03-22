""" This program allows user to access two financial calculators: 
an investment and a home loan repayment calculator.

"""


import math

divider = "-"*0
message = "Welcome to the Financial Calculator!"
print(divider)
print(message)
print(divider)
# The user chooses which calculator to use

print("investment - to calculate the amount of interest " 
      "you'll earn on your investment \n" 
      "bond       - to calculate the amount you'll have to pay on a home loan")
print()

user_choice = input("Enter either \'investment\' or \'bond\' " 
                    "from the menu above to proceed: \n")
user_choice_lower = user_choice.lower()  # the calculator will work regardless of the capital letters in the input, if the user inputs such.


# Collecting input for investment calculations 

if user_choice_lower == "investment":
    deposit = input("How much money do you want to deposit? \n")
    deposit = float(deposit)
    interest_rate_inv = input("What is your interest rate? \n")
    interest_rate_inv = float(interest_rate_inv)
    interest_rate_for_formulae = interest_rate_inv/100
    years = input("How many years do you plan on investing? \n")
    years = int(years)


 # User selects the kind of interest he wants

    interest = input("Which interest do you want: simple or compound? \n")
    interest_lower = interest.lower()

    # Calculating simple interest

    if interest_lower == "simple":  
        total_simple = deposit*(1+interest_rate_for_formulae*years)
        print(f"After {years} years you will get £ {total_simple}.")

    # Calculating compound interest

    elif interest_lower == "compound": 
        total_compound = deposit*math.pow((1+interest_rate_for_formulae),years)
        print(f"After {years} years you will get £ {total_compound}.")
 
    # Error message if user enters the wrong word when choosing the kind of interest
 
    else:  
        print("Make sure you enter the word \"simple\" for simple interest or the word \"compound\" for compound interest.")


# Collecting input for bond calculator

elif user_choice_lower == "bond":
    value = input("What is the present value of your house?\n")
    value = int(value)
    inter_rate_bond = input("What is your interest rate? \n")
    inter_rate_bond = int(inter_rate_bond)
    inter_rate_bond_formulae = inter_rate_bond/100
    inter_rate_bond_month = inter_rate_bond_formulae/12
    time_bond = input("How many month do you plan to take to repay the bond? \n")
    time_bond = int(time_bond)
    

    # Calculating the bond

    repayment = (inter_rate_bond_month * value)/(1 - (1 + inter_rate_bond_month)**(- time_bond))
    print(f"You will have to repay £ {repayment} each month for {time_bond} months.")

# Error message if the user enters a wrong word when choosing a calculator
else:
    print("Make sure you enter the word \" investment\" or the word \"bond\".")
