print("Welcome to the Price Comparison Tool")
print()

budget = input("How much money are you wanting to spend? ")
def budget_checker (question, low, high):
  error = "please enter a whole number between 1 and 1000; we do not allow numbers above 1000 as we don't have change\n"
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

budget = budget_checker ("How much money are you wanting to spend ", 0,1000)
print("You will be spending ${}".format(budget))
print()