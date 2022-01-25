# functions for calculating tip

def greeting():
    """This greets the user."""
    return print("Welcom to the tip calculator and bill splitter ")

def run_program():
    """This runs program until user invokes the quite function"""
    pass

def end_program():
    """This ends the program"""
    pass

def get_bill():
    """Gets total bill from user."""
    return input("\nPlease enter the total bill amount: \n")

def get_tip_percent():
    """Gets desired tip percentage from user."""
    return input("\nPlease enter the desired tip percentage: \n")

def get_number_of_people():
    """Gets number of people to split total bill between"""
    return input("\nPlease enter the number of people to split the bill: \n")


def calc_tip_amount(bill, tip_percent):
    """Calculates the tip given total bill and tip percent.
    
    Args:
      bill: the bill
      tip_percent: desired tip percent

    Returns:
      The calculated tip amount.

    """
    return bill * tip_percent

def calc_total_bill(tip, bill):
    """Calculates the total bill which includes tip
    
    Args:
      tip:
      bill:

    Returns:
      Total bill. 
    """
    return bill + tip

def split_bill(total_bill, number_of_people):
    """Splits bill based on user input."""
    return print(f"Each person should pay: ${total_bill / number_of_people}")
