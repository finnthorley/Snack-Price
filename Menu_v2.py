def reply():
  print()
  print("Thanks for stopping by!")

def menu():
  print()
  print("Menu                                |  Price    |")
  print()
  print("Sea Salt Crackers                   |  $2.00    |")
  print()
  print("Griffins Snax                       |  $2.50    |")
  print()
  print("Pizza Shapes                        |  $3.30    | ")
  print()
  print("Arnotts Cheds                       |  $3.99    |")
  print()
  print("Rosemary Wheat                      |  $2.00    |")
  print()
  print("Original Rice Crackers              |  $1.65    |")

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

 

if display_menu == "no" or display_menu == "n":
  reply()


if display_menu == "yes" or display_menu == "y":
  print()
  print("Preparing Menu...")
menu()


  


  
