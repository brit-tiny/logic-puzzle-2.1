# GPT-4.1

def print_intro():
    print("Welcome to the River Crossing Puzzle!")
    print("A farmer must transport a fox, a goose, and a bag of grain across a river.")
    print("The boat can only hold the farmer and one other item at a time.")
    print("Rules:")
    print("- The fox cannot be left alone with the goose (the fox will eat the goose).")
    print("- The goose cannot be left alone with the grain (the goose will eat the grain).")
    print("Your goal: Get all three items across the river safely.")
    print()


def print_state(left, right, boat):
    print(f"\nLeft bank: {', '.join(left) if left else 'none'}")
    print(f"Right bank: {', '.join(right) if right else 'none'}")
    print(f"Boat is on the {boat} bank.")


def is_valid(bank):
    # If farmer is present, no danger
    if 'farmer' in bank:
        return True
    # If fox and goose alone
    if 'fox' in bank and 'goose' in bank:
        return False
    # If goose and grain alone
    if 'goose' in bank and 'grain' in bank:
        return False
    return True


def prompt_move(options):
    print("\nWho or what will the farmer take across the river?")
    print("Options:", ', '.join(options + ['none (farmer goes alone)']))
    choice = input("Enter your choice: ").strip().lower()
    return choice


def main():
    print_intro()
    left = ['farmer', 'fox', 'goose', 'grain']
    right = []
    boat = 'left'

    while True:
        print_state(left, right, boat)
        if set(right) == {'farmer', 'fox', 'goose', 'grain'}:
            print("\nCongratulations! You solved the puzzle.")
            break
        # Determine who can go
        current_bank = left if boat == 'left' else right
        options = [item for item in current_bank if item != 'farmer']
        move = prompt_move(options)
        if move == 'none' or move == 'farmer goes alone' or move == '':
            move = None
        elif move not in options:
            print("Invalid choice. Try again.")
            continue
        # Move farmer and possibly one item
        if boat == 'left':
            left.remove('farmer')
            right.append('farmer')
            if move:
                left.remove(move)
                right.append(move)
            boat = 'right'
        else:
            right.remove('farmer')
            left.append('farmer')
            if move:
                right.remove(move)
                left.append(move)
            boat = 'left'
        # Check for danger
        if not is_valid(left):
            print_state(left, right, boat)
            print("\nOh no! Something got eaten on the left bank. Game over.")
            break
        if not is_valid(right):
            print_state(left, right, boat)
            print("\nOh no! Something got eaten on the right bank. Game over.")
            break

if __name__ == "__main__":
    main()
