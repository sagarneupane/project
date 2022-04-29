
import random

def numberGuessing(low,n):
    low = low
    high = n
    guess_number = random.randrange(low,high)
    user_input = input(f'The computer guess {guess_number} is it Correct? Low? or High ? ')
    return user_input,guess_number,low,high

def evaluateResult(low,high):
    user_input,guess_number,low,high = numberGuessing(low, high)
    
    if user_input =="h":
        low = low
        high = guess_number-1
        evaluateResult(low, high)
    elif user_input == "l":
        high = high
        low = guess_number +1
        evaluateResult(low, high)
    else:
        print(f"Yay !! Computer Guessed your Number {guess_number}")

low = int(input("Enter The Lowest Range from which computer need to guess: ")) 
high = int(input("Enter the highest Range from which computer need to guess: "))
evaluateResult(low, high)
# a = numberGuessing(0,100)
# print(a)
