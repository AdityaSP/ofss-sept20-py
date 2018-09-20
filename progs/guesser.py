import random
r = random.randint(1,100)

print("I have thought of a number. Its your turn to guess.")
while True:
    ui = int(input("Enter you guess[1,100] :"))
    if ui < r:
        print("Low")
    elif ui > r:
        print("High")
    else:
        print("You guessed it right!")
        break