import random

attempts = 0
num = random.randint(0, 100)

while True:
    user_input = input('Guess a number between 0 and 100: ')
    
    # Input validation to handle non-integer inputs
    try:
        user_input = int(user_input)
    except ValueError:
        print("Please enter a valid integer.")
        continue

    attempts += 1

    if user_input < num:
        print('Too low!')
    elif user_input > num:
        print('Too high!')
    else:
        break

print('Correct!')
print('Number of attempts:', attempts)