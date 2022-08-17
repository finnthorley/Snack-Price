def yes_no(question):
  valid = False
  while not valid:
    response = input(question).lower()

    if response == "yes" or response == "y":
      response = "yes"
      return response

    elif response == "no" or response == "n":
      response = "no"
      return response

    else:
      print ("Please type yes/no")


display_menu = yes_no("Would you like to see the menu? ")

if display_menu == "yes" or if display_menu == "y":
  
  
