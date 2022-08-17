print("Welcome to the Price Comparison Tool")
print()

def price_check (question, low, high):
  error = "Please enter a whole number between 1 and 1000; we do not allow numbers above 1000 as we don't have change\n"
  valid =  False 
  while not valid:
    try:
      response = float(input(question))

      if 0 < response < 1000:
        return response
      else:


        print(error)
    except ValueError:
      print(error)

price = price_check ("How much money are you wanting to spend? ", 0,1000)
print("You will be spending ${}".format(price))
print()