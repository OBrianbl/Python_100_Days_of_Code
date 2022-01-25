# Author: Brandon
# Date: 2022.01.24
# Description: This program is the 1st challenge in the 100 Days of Code: Python that 
# generates a band name using input from the user and prints it to the screen

def greeting():
    """Welcomes User to Band Name Generator

    Args:
      NONE
    
    Returns:
      Welcome message
    
    Raises:
      NONE
    """
    return print("Welcome to the band name generator!\n")

def request_pet_name():
    """Requests users pet name as input.
    
    Args: 
      NONE
    
    Returns:
      User's name. 
    
    Raises:
      ValueError: If input is not a character. 
    """
    while True:
      try:
        if (pet_name := input("Enter your pet's name: \n")).isalpha():
            break
        else:
          print("Must be characters, please enter your pet's name again.")
      except ValueError:
        print("Provide name with only characters.")
        continue
    return pet_name


def request_city_name():
    """Function requests the city the user lives in and assigns the result.

    Args:
      NONE

    Returns:
      city: User's city

    Raises: 
      ValueError: If User's input is not character. 
    """
    while True:
      try:
        if (city := input("\nEnter the city name where you live: \n")).isalpha():
            break
      except ValueError:
        print("Provide name with only characters.")
        continue
    return city

# genearate_band_name
def generate_band_name(name, city):
    """Generates band name given users input for name and city.
    
    Args:
      name: User's name
      city: User's city

    Returns:
      Band name generated via User's name and city

    Raises:
      NONE
    """
    return print("\nYour band name is: {} {}\n\nThank you for your participation!\n".format(city, pet_name))


if __name__ == "__main__":
    greeting()
    pet_name = request_pet_name()
    city = request_city_name()
    generate_band_name(pet_name, city)