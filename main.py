import time

print("Welcome to the Price Comparison Tool")
print()

price = 0

item = ""

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

def budget_changer (question, low, high):
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

def repli():
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


display_menu = yes_no("Would you like to see the menu? ")

 

if display_menu == "no" or display_menu == "n":
  reply()


if display_menu == "yes" or display_menu == "y":
  print()
  print("Preparing Menu...")
  menu()

def food(question):
  valid = False
  while not valid:
    response = input(question).lower()

    if response == "Sea Salt Crackers" or response == "a":
      response = "Sea Salt Crackers"
      global price
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
      print()
      print("Please select an item that is on the menu")
      print()

want_order = yes_no("Would you like to order now? ").lower()
if want_order == "no" or want_order == "n":
  repli()
  time.sleep(10)
  want_order = yes_no("Would you like to order now? ")
if want_order == "no" or want_order == "n":
    reply()
    time.sleep(10)
    want_order = yes_no("Would you like to order now? ")
    
  

if want_order == "yes" or want_order == "y":
  print()
 


would_like = food ("What can I get you today? ").lower()


if budget < price: 
  print("You've picked an item that's more than your budget")
  


change = budget - price
price 
if price > budget:
  print("The item you are buying exceeds your budget ")
  time.sleep(5)
  print()
  print("You will need to increase your budget to ${} to purchase the item".format(price))
  time.sleep(5)
  print()
  
  while True:
    exit = ("| type a if want to change your budget or type b if you want to exit the program : ").lower()
    print()

    if exit == "a":
      while True:
        new_budget = budget_changer("Please enter your new budget : ", price, 1000)
  
        if new_budget >= price:
          print("A {} will cost ${}".format(item, price))
          change = new_budget - price
          rounded_change = round(change, 2)
          print("Your change is ${}".format(rounded_change))
          print("Thanks for visting us")
          exit()

        else:
          print()
          print("please enter a whole number that is greater than {} but less than 1000".format(price))
      
    
    elif exit == "b":
      print("Thanks for stopping by")
      exit()
      

         

  




 