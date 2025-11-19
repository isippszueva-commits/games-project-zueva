import random
from .engine import run

def even_odd_game_logic(player_name):

    number = random.randint(1, 100)
    correct_answer = "even" if number % 2 == 0 else "odd"

    print(f"Is the number {number} even or odd?")
    user_answer = input("Your answer (even/odd): ").lower()

    if user_answer == correct_answer:
        print("Correct!")
        return True
    else:
        print(f"'{user_answer}' is wrong. The correct answer was '{correct_answer}'.")
        return False

def play_even():

    run(even_odd_game_logic, greeting="Welcome to the Even/Odd challenge!", name_prompt="Your name?")

