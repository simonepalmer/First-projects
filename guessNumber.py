# Imports
import random
import ast

def welcome_to_the_game():
    name = input("What's your name?: ")
    print(f"\nHello, {name}!")
    return name 

def decide_upper_range():
    upper_range = check_type(input("Enter upper range: "))
    while upper_range < 20 or upper_range > 1000:
        if upper_range < 20:
            print("\nThat seems a bit too easy, it should probably at least 20!")
            upper_range = check_type(input("Try again: "))
        else:
            print("\nThat seems a bit too high, we dont want to be here all day! Maybe 1000 at most?")
            upper_range = check_type(input("Try again: "))
    print(f"\nGood! I'll be thinking of a number between 1 and {upper_range}")
    return upper_range 

def decide_my_max_guesses(upper_range):
    my_max_guesses = check_type(input("Enter max number of guesses: "))
    # Adjusting appropriate guesses based on range
    appropriate_max = 7 if upper_range > 99 else 5
    if upper_range > 499: appropriate_max = 10
    appropriate_min = 3 if upper_range < 251 else 4
    if upper_range < 51: appropriate_min = 2
    while my_max_guesses > appropriate_max or my_max_guesses < appropriate_min:
        if my_max_guesses > appropriate_max:
            print(f"\nThat seems a bit too easy based on the range, it should probably be {appropriate_max} at most!")
            my_max_guesses = check_type(input("Try again: "))
        else:
            print(f"\nThat seems a bit too hard based on the range, it should probably be {appropriate_min} at least!")
            my_max_guesses = check_type(input("Try again: "))
    print("\nSure, that seems reasonable")
    return my_max_guesses

def print_hint_string(my_guess, hidden_number):        
        guess_dif = hidden_number - my_guess
        if guess_dif < -75 or guess_dif > 75: # How far off?
            hint = "WAY "
        elif guess_dif < -25 or guess_dif > 25:
            hint = "much "
        elif guess_dif < -7 or guess_dif > 7:
            hint = ""
        elif guess_dif < -3 or guess_dif > 3:
            hint = "a little bit "
        elif guess_dif < -1 or guess_dif > 1:
            hint = "just a little bit "
        elif guess_dif == -1 or guess_dif == 1:
            hint = "so close! just a little bit "
        if my_guess > hidden_number: # Too high or too low?
            direction = "lower."
        else:
            direction = "higher."
        print(f"\nThat is not correct. My number is {hint}{direction}")

def game_over_or_win(my_max_guesses,my_used_guesses, hidden_number):
    if my_used_guesses >= my_max_guesses:
        print(f"\nGAME OVER!\nYou are out of guesses, the correct number was {hidden_number}.\n")
    else:
        print(f"\nTHAT IS CORRECT!\nI was indeed thinking of {hidden_number}!\n")

def check_type(input_type):
    while type(input_type) != int:
        try: # set type based on input (default string, preferred int)
            input_type = ast.literal_eval(input_type)
        except (ValueError, SyntaxError):
            pass
        if type(input_type) == float: # Giving hints based on wrong type input
            input_type = input("\nPlease enter a number(int), not a number with decimals(float) Try again: ")
        elif type(input_type) == str:
            input_type = input("\nPlease enter a number(int), not a word(string). Try again: ")
        else:
            break
    return input_type

def main():
    name = welcome_to_the_game()
    # Decide difficulty
    print("\nI'm going to think of a number and your are going to guess it. What range do you think is reasonable? 1 to what?")
    upper_range = decide_upper_range()
    hidden_number = random.randint(1, upper_range)
    print("\nHow many guesses do you need?")
    my_max_guesses = decide_my_max_guesses(upper_range)
    # Game starts
    my_used_guesses = 0
    my_guess = input("\nLet's start! What number am I thinking of?\nGuess a number: ")
    while str(my_guess) != str(hidden_number):
        my_guess = check_type(my_guess)
        hint_string = print_hint_string(my_guess, hidden_number)
        my_used_guesses += 1
        guesses_left = my_max_guesses - my_used_guesses
        if my_used_guesses == my_max_guesses:
            break
        if my_used_guesses == my_max_guesses-1:
            print(f"only {guesses_left} guess left...")
        else:
            print(f"{guesses_left} guesses left")
        my_guess = input("\nGuess again: ")
    # Game over
    game_over_or_win(my_max_guesses, my_used_guesses, hidden_number)

if __name__ == "__main__":
    main()