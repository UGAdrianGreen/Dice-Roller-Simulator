import random

def roll_single_die():
    return random.randint(1, 6)

def roll_multiple_dice(num_dice):
    return [random.randint(1, 6) for _ in range(num_dice)]

def main():
    print("Welcome to the Dice Rolling Simulator!")
    while True:
        print("\nMenu:")
        print("1. Roll a single die")
        print("2. Roll multiple dice")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            print("You rolled:", roll_single_die())
        elif choice == '2':
            num_dice = int(input("Enter the number of dice to roll: "))
            print("You rolled:", roll_multiple_dice(num_dice))
        elif choice == '3':
            print("Thank you for using the Dice Rolling Simulator. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
