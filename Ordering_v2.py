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

 