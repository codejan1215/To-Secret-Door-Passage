def theDoorNeedsCodeAndKey(has_key, has_code):
    if has_key and has_code:
        print("\nYou use the key and the code to unlock the door. Congratulations! You've won the game!")
        return True
    else: 
        print("\nYou must have both the key and the code to unlock the door. Continue searching.")
        return False

def explore_library(has_code):
    if has_code:
        print("\nYou've already solved the library puzzle and obtained the code.")
        return has_code

    print("\nYou enter the library. A mysterious voice asks you a riddle:")
    print("I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?")
    answer = input("Your answer: ").strip().lower()

    if answer == "echo":
        print("\nCorrect! You've obtained the code.")
        return True
    else:
        print("\nIncorrect. You leave the library empty-handed.")
        return False

def explore_armory(has_key):
    if has_key:
        print("\nYou've already obtained the key from the armory.")
        return has_key

    print("\nYou enter the armory. A guard challenges you to a simple math problem:")
    print("What is 7 + 5?")
    answer = input("Your answer: ").strip()

    if answer == "12":
        print("\nCorrect! You've obtained the key.")
        return True
    else:
        print("\nIncorrect. You leave the armory empty-handed.")
        return False

def try_bag(has_key, has_code):
    if has_key and has_code:
        print("\nYou can now use it to unlock the door.")
        return True
    elif not has_key and not has_code:
        print("\nYou still need both the key and the code.")
    elif not has_key:
        print("\nYou still need the key.")
    elif not has_code:
        print("\nYou still need the code.")
    return False

def show_menu():
    print("\nWhat would you like to do?")
    print("1. Explore the library")
    print("2. Explore the armory")
    print("3. Check bag")
    print("4. Magic Door")
    print("5. Quit")
    
    choice = input("Enter your choice (1-5): ").strip()
    return choice

def main():
    has_key = False
    has_code = False

    while True:
        choice = show_menu()

        if choice == "1":
            has_code = explore_library(has_code)
        elif choice == "2":
            has_key = explore_armory(has_key)
        elif choice == "3":
            try_bag(has_key, has_code)
        elif choice == "4":
            if theDoorNeedsCodeAndKey(has_key, has_code):
                break
        elif choice == "5":
            print("Thank you for playing! Goodbye.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

main()