NUMBER_OF_ROUNDS = 3

def run(game_logic_function, greeting="Welcome to the VD games!", name_prompt="May I have your name?"):
    print(greeting)
    name = input(name_prompt + " ")
    print(f"Hello, {name}!")

    correct_answers_count = 0
    for _ in range(NUMBER_OF_ROUNDS):
        if game_logic_function(name):
            correct_answers_count += 1
        else:
            print(f"Let's try again, {name}!")
            return

    if correct_answers_count == NUMBER_OF_ROUNDS:
        print(f"Congratulations, {name}!")
    else:
        print(f"You answered {correct_answers_count} out of {NUMBER_OF_ROUNDS} questions correctly, {name}. Keep practicing!")