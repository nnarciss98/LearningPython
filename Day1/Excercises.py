#FizzBuzz:
import random


def fizzbuzz():
    for i in range(100):
        if i % 3 == 0:
            print("{}: FizzBuzz".format(i)) if i % 5 == 0 else print("{}: Fizz".format(i))
        if i % 5 == 0:
            print("{}: Buzz".format(i))

#Number guesser game
def guessnumber():
    rand = random.randint(0, 100)
    print(rand)
    guess = int(input("Guess the number: "))
    while guess != rand:
        if guess > rand:
            guess = int(input("Wrong number, guess lower! "))
        else:
            guess = int(input("Wrong number, guess higher! "))
    print("Congratulations! The right number was {} indeed".format(rand))




print("######################### FizzBuzz #########################")
fizzbuzz()
print("######################### Guess number game #########################")
guessnumber()