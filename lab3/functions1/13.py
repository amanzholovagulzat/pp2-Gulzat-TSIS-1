import random
name = input("Hello! What is your name?\n")

print( f"Well,{name}, I am thinking of a number between 1 and 20.")
number = random.randint(1, 20)
numb = 0
guesses = 0
while numb != number:
        numb = int(input("Take a guess.\n"))
        guesses += 1
        if numb < number:
            print("Your guess is too low.")
        elif numb > number:
            print("Your guess is too high.")
print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
    

