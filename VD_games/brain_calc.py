import random

def generate_question():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    op = random.choice(['+', '-', '*'])

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    else:
        result = num1 * num2

    question = f"{num1} {op} {num2}"
    return question, str(result)