print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

from random import randint
my_guess = randint(0, 100)
guess_list = [0]
while True:
 # we can copy the code from above to take an input
    u_guess = int(input('Guess a number!!, I am thinking between 1 and 100'))
    guess_list.append(u_guess)
    # print(result)
    if (u_guess < 1 or u_guess > 100):
        print("I am sorry!, you are OUT OF BOUNDS!!!")
        continue

    if (u_guess == my_guess):
        print(f'Congratulations! your guess is correct!, you took {len(guess_list)} guesses')
        break

    if guess_list[-2]:
        if (abs(my_guess - u_guess) < abs(my_guess - guess_list[-2])):
            print("WARMER!!")
        else:
            print('COLDER!!')
    else:
        if (abs(my_guess - u_guess) <= 10):
            print("warm")
        else:
            print("cold")