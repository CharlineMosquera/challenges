#!/usr/bin/python3
def fizzbuzz():
    print("""
    THE FIZZ-BUZZ GAME
    how to play?
    >> You must enter the numbers from 1 to 100
    >> If the number is divisible by 3 enter "Fizz"
    >> If the number is divisible by 5 enter "Buzz"
    >> If the number is divisible by 3 and by 5 type "FizzBuzz".

    You have 3 lives
    Each correct answer is worth 10 points
    For each wrong answer you lose 10 points and 1 life.
    """)
    score = 0
    lives = 3
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            result = "FizzBuzz"
        elif i % 3 == 0:
            result = "Fizz"
        elif i % 5 == 0:
            result = "Buzz"
        else:
            result = i
        user = input(f"Type the value {i}: ")
        if str(result) == user:
            score += 10
            print(f"Correct!!\nYour score is {score}\n")
        else:
            lives -= 1
            score -= 10
            print(f"Fail :(\nYour score is {score}\nYour lives are: {lives}\n")
        if lives == 0:
            print("Game Over!")
            return
        if score == 1000:
            print("You are unbeaten")
        if i == 100:
            print("You have completed the game. Congratulations.")
