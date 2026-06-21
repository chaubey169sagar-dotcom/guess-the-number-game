import random

secret_number= random.randint(1,100)

while True:
    try:
      guess=int(input("guess the number"))

      if guess > secret_number:
        print("high")
      elif guess<secret_number:
        print("low")
      elif guess== secret_number:
        print("you won")
        break
    except ValueError:
      print("please entr valid number")  
