print("Welcome to the Price Comparison Tool")
print()

def budget_checker (question, low, high):
  error = "Please enter a whole number between 1 and 1000; we do not allow numbers above 1000 as we don't have change.\n"
  valid =  False 
  while not valid:
    try:
      response = float(input(question))

      if 0 < response <= 1000:
        return response
      else:


        print(error)
    except ValueError:
      print(error)

budget = budget_checker ("How much money are you wanting to spend? ", 0,1000)
print()
print("You will be spending ${}".format(budget))
print()
def reply():
  print()
  print("Thanks for stopping by!")
  exit()

def menu():
  print()
  print("Menu                                   |  Price    |")
  print()
  print("Sea Salt Crackers (A)                  |  $2.00    |")
  print()
  print("Griffins Snax (B)                      |  $2.50    |")
  print()
  print("Pizza Shapes (C)                       |  $3.30    | ")
  print()
  print("Arnotts Cheds (D)                      |  $3.99    |")
  print()
  print("Rosemary Wheat (E)                     |  $2.00    |")
  print()
  print("Original Rice Crackers (F)             |  $1.65    |")
  print()
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
  
if display_menu == "yes" or display_menu == "y":
    menu()
if display_menu == "no" or display_menu == "n":
  reply()

import time 


def reply():
  print()
  print("I'll give you a moment.")
  print()





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
  reply()
  time.sleep(10)
  want_order = yes_no("Would you like to order now? ")
if want_order == "no" or want_order == "n":
    reply()
    time.sleep(10)
    want_order = yes_no("Would you like to order now? ")
    
  

if want_order == "yes" or want_order == "y":
  print()
  print("What can I get you today?")

 