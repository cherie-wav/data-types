import random
n = random.randint(1,100)
guesses=None
guesses=1
guess_history = []
for i in guess_history:
     print (guess_history)
guess = int(input("enter any number: "))
while n!= guess:
    if guess < n:
        print('higher!')
        guesses += 1
        guess_history.append(guess)
        print(f"your guesses were: {guess_history}")
        guess = int(input("try again!"))
        if guess == n:
                print(f"you got it! you took {guesses} tries")
    elif guess > n:
        print('lower!')
        guesses += 1
        guess_history.append(guess)
        print(f"your guesses were: {guess_history}")
        guess = int(input("try again!"))
        if guess == n:
                print(f"you got it! you took {guesses} tries")
    else:
        print(f"you got it! you took {guesses} tries")
        print(f"your guesses were: {guess_history}")
        break