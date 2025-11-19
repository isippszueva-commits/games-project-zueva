import random

def is_prime(number):

    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    i = 3
    while i * i <= number:
        if number % i == 0:
            return False
        i += 2
    return True

def generate_prime_question():

    number = random.randint(2, 100)
    correct_answer = "yes" if is_prime(number) else "no"
    question_string = f"Question: {number}"
    return question_string, correct_answer


def main():

    print("VD-prime")
    print("Welcome to the VD Games!")
    player_name = input("May I have your name? ")
    print(f"Hello, {player_name}!")

    print("Answer \"yes\" if given number is prime. Otherwise answer \"no\".")

    rounds_to_play = 3

    for i in range(rounds_to_play):
        question_str, correct_ans = generate_prime_question()

        print(f"\n{question_str}")

        while True:
            user_answer_str = input("Your answer: ").lower()
            if user_answer_str in ['yes', 'no']:
                break
            else:
                print("Invalid input. Please answer 'yes' or 'no'.")

        if user_answer_str == correct_ans:
            print("Correct!")
        else:
            print(f"'{user_answer_str}' is wrong answer ;(. Correct answer was '{correct_ans}'.")
            print(
                f"Let's try again, {player_name}!")

    print(f"\nCongratulations, {player_name}!")

