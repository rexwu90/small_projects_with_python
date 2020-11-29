import random
number = random.randint(1, 100)
low_number = 0
high_number = 100
guess = 0
print('I am thinking of a number between 1 and 100.')

while guess != number:
    print('Take a guess')
    guess = int(input())

    if guess < number:
        if guess < low_number:
            print('The number not right!')
            print('The number between %d and %d.' % (low_number, high_number))
        else:
            low_number = guess
            print('The number between %d and %d.' % (low_number, high_number))
    elif guess > number:
        if guess > high_number:
            print('The number not right!')
            print('The number between %d and %d.' % (low_number, high_number))
        else:
            high_number = guess
            print('The number between %d and %d.' % (low_number, high_number))

print('Good job! You guessed my number')