from VD_games.VD_even import play_even
from VD_games.VD_calculator import play_calculator
from VD_games.VD_gcd import play_gcd

from scripts.VD_progression import main as play_progression
from scripts.VD_prime import main as play_prime

def main():
    print("Choose a game to play:")
    print("1. Even/Odd Game")
    print("2. Calculator Game")
    print("3. GCD Game")
    print("4. Progression Game")
    print("5. Prime Number Game")


    choice = input("Enter your choice (1, 2, 3, 4, 5): ")

    if choice == '1':
        play_even()
    elif choice == '2':
        play_calculator()
    elif choice == '3':
        play_gcd()
    elif choice == '4':
        play_progression()
    elif choice == '5':
        play_prime()
    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, 5")


if __name__ == '__main__':
    main()

