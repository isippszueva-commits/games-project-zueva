from VD_games.VD_even import play_even
from VD_games.VD_calculator import play_calculator
from VD_games.VD_gcd import play_gcd

def main():
    print("Choose a game to play:")
    print("1. Even/Odd Game")
    print("2. Calculator Game")
    print("3. GCD Game")
    choice = input("Enter your choice (1, 2, 3): ")

    if choice == '1':
        play_even()
    elif choice == '2':
        play_calculator()
    elif choice == '3':
        play_gcd()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == '__main__':
    main()

