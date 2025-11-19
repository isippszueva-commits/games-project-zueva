import math
import random

def gcd_game_logic(player_name):
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct_answer = str(math.gcd(num1, num2))

    print(f"Find the greatest common divisor of {num1} and {num2}.")
    user_answer = input("Your answer: ")

    if user_answer == correct_answer:
        print("Correct!")
        return True
    else:
        print(f"'{user_answer}' is wrong answer :( Correct answer was '{correct_answer}'.")
        return False

def play_gcd():
    from .engine import run

    run(gcd_game_logic, greeting="Welcome to GCD game!", name_prompt="What's your name?")


