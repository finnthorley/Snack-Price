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

would_like = food ("What can I get you today?")

if would_like == "Sea Salt Crackers" or would_like == "A":
  print("That will come to a total of $2.00.")

if would_like == "Griffins Snax" or would_like == "B":
  print("That will come to a total of $2.50.")

if would_like == "Pizza Shapes" or would_like == "C":
  print("That will come to a total of $3.30.")

if would_like == "Arnotts Cheds" or would_like == "D":
  print("That will come to a total of $3.99.")

if would_like == "Rosemary Wheat" or would_like == "E":
  print("That will come to a total of $2.00.")

if would_like == "Original Rice Crackers" or would_like == "F":
  print("That will come to a total of $1.65.")



  

 