import time 


def reply():
  print()
  print("I'll give you a moment.")
  print()


def food(question):
  valid = False
  while not valid:
    response = input(question).lower()

    if response == "Sea Salt Crackers" or response == "a":
      response = "Sea Salt Crackers"
      price = 2
      print("Sea Salt Crackers will come to a total of ${}.".format(price))
      return response

    elif response == "Griffins Snax" or response == "b":
      response = "Griffins Snax"
      price = 2.5
      print("Griffins Snax will come to a total of ${}.".format(price))
      return response

    elif response == "Pizza Shapes" or response == "c":
      response = "Pizza Shapes"
      price = 3.3
      print("Pizza Shapes will come to a total of ${}.".format(price))
      return response

    elif response == "Arnotts Cheds" or response == "d":
      response = "Arnotts Cheds"
      price = 3.99
      print("Arnotts Cheds will come to a total of ${}.".format(price))
      return response

    elif response == "Rosemary Wheat" or response == "e":
      response = "Rosemary Wheat"
      price = 2
      print("Rosemary Wheat will come to a total of ${}.".format(price))
      return response

    elif response == "Original Rice Crackers" or response == "f":
      response = "Original Rice Crackers"
      price = 1.65
      print("Original Rice Crackers will come to a total of ${}.".format(price))
      return response

    else:
      print ("Choose an item from the Menu please.")





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



want_order = yes_no("Would you like to order now? ")
if want_order == "no" or want_order == "n":