name: str = input("What is your name?: ").lower()
age: int = int(input("What is your age?: "))

print(f'Hello, {name}! You are {age} years old.')

try:
    question: str = input("Do you know what year you will turn 100?: ").lower()
    if question == 'no':
        print("That's okay! You can calculate it by adding 100 to your current age.")
        year_turn_100: int = 2026 + (100 - age)
        print(f"You will turn 100 in the year {year_turn_100}.")
    else: 
        year: int = int(input("What year will you turn 100?: "))
        if year == 2026 + (100 - age):
            print(f"Correct! You will turn 100 in year {year}.")
        else:
            print(f"Incorrect. You will turn 100 in the year {2026 + (100 - age)}.")
except ValueError:
    print("Please enter a valid number for your age and year.")
    
try:
    if age < 13:
        print("You are a young coder.")
    elif 13 < age < 17:
        print("You are a teenage coder.")
    elif age >= 17:
        print("You are an adult coder.")
except ValueError:
    print("Please enter a valid number for your age.")
    