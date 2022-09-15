price = 0 

item = ""

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


budget = budget_checker ("| How much money are you wanting to spend : ", 0,1000)
print()
print("| You will be spending ${}".format(budget))
print()

change = budget - price

if price > budget:
  print("| The item you are buying exceeds your budget ")
  print()
  print("| You will need to increase your budget to ${} to purchase the item".format(price))
  print()
  while True:
    exit = ("| type Change if want to change your budget or type Exit if you want to leave : ").lower()
    print()

    if exit == "exit":
      
      while True:
        new_budget = budget_changer("| How much money are you wanting to spend : ", price, 1000)
  
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
         
    #ask user if they wish to leave
    if exit == "b":
      print("OK have a nice day")
      exit()