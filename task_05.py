import random

print("Number Guessing Game!")
print("Guess a number between 1-50. You have 5 attempts.\n")

secret_number = random.randint(1, 50)
attempts_left = 5

while attempts_left > 0:
    try:
        guess = int(input(f"Attempt {6-attempts_left}/5 - Enter your guess: "))
        
        if guess < 1 or guess > 50:
            print("Please enter a number between 1-50!")
            continue
        
        if guess == secret_number:
            print(f"\n🎉 Congratulations! You guessed it right! The number was {secret_number}.")
            break
        
        attempts_left -= 1
        
        if guess < secret_number:
            hint = "higher"
        else:
            hint = "lower"
            
        print(f"Wrong! Try a {hint} number. Attempts left: {attempts_left}")
        
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

if attempts_left == 0:
    print(f"\nGame over! The secret number was {secret_number}.")
