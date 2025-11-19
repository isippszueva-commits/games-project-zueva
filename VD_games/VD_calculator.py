import random
import operator
from .engine import run

operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}

def calculate_game_logic(player_name):

    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operation_symbol = random.choice(list(operations.keys()))
    operation = operations[operation_symbol]

    question = f"{num1} {operation_symbol} {num2} = ?"
    try:
        correct_answer = str(operation(num1, num2))
    except ZeroDivisionError:
        print("An internal error occurred. Please try again.")
        return False

    print(f"Question: {question}")
    user_answer = input("Your answer: ")

    if user_answer == correct_answer:
        print("Correct!")
        return True
    else:
        print(f"'{user_answer}' is wrong. The correct answer was '{correct_answer}'.")
        return False

def play_calculator():

    run(calculate_game_logic, greeting="Welcome to the Calculator!", name_prompt="Your name?")

