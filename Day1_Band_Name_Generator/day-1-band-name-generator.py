# Author: Brandon
# Date: 2022.01.24
# Description: This program is the 1st challenge in the 100 Days of Code: Python that 
# generates a band name using input from the user and prints it to the screen



def request_name():
    """Requests users name as input.
    
    Args: 
      NONE
    
    Returns:
      User's name. 
    
    Raises:
      ValueError: If input is not a character. 
    """
    while True:
      try:
        if (name := input("Enter your first name: ")).isalpha():
            break
        else:
          print("Must be characters, please enter your name again.")
      except ValueError:
        print("Provide name with only characters.")
        continue
    return name


def request_city_name():
    """Function requests the city the user lives in and assigns the result.

    """
    while True:
      try:
        if (city := input("Enter the city name where you live: ")).isalpha():
            break
      except ValueError:
        print("Provide name with only characters.")
        continue
    return city

# genearate_band_name
def generate_band_name(input1, input2):
    """Generates band name given users input for name and city.
    
    Args:
      input1:
      input2:

    Returns:

    Raises:
    """
    return print("Your band name is: {} {}".format(input1, input2))


if __name__ == "__main__":
    name = request_name()
    street = request_city_name()
    generate_band_name(name, street)