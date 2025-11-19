import random


def generate_arithmetic_progression():

    length = random.randint(5, 10)
    start_element = random.randint(1, 50)
    step = random.randint(2, 10)

    progression_numbers = []
    for i in range(length):

     progression_numbers.append(start_element + i * step)

    hidden_index = random.randint(0, length - 1)
    correct_answer = progression_numbers[hidden_index]

    display_list = progression_numbers[:]
    display_list[hidden_index] = '..'

    question_string = ' '.join(map(str, display_list))

    return question_string, correct_answer

def main():

    print("VD-progression")
    print("Welcome to the VD Games!")
    player_name = input("May I have your name? ")
    print(f"Hello, {player_name}!")
    rounds_to_play = 3

    for i in range(rounds_to_play):
        question_str, correct_ans = generate_arithmetic_progression()

        print(f"\nWhat number is missing in the progression?")
        print(f"Question: {question_str}")

        while True:
            try:
                user_answer_str = input("Your answer: ")
                user_answer = int(user_answer_str)
                break
            except ValueError:
                print("Invalid input. Please enter a whole number.")

        if user_answer == correct_ans:
            print("Correct!")
        else:
            print(f"'{user_answer_str}' is wrong answer ;(. Correct answer was '{correct_ans}'.")
            print(f"Let's try again, {player_name}!")

    print(f"\nCongratulations, {player_name}!")
