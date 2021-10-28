import random
game = 1
while game != 0:
    user = int(input("Guess a number between 1 to 5 "))
    randomNumber = random.randint(1, 5)
    if user == randomNumber:
        print("You have won")
    elif user < randomNumber:
        print("Your guess is too low, the correct number is " + str(randomNumber))
    elif user > randomNumber:
        print("Your guess is too high, the correct number is " + str(randomNumber))