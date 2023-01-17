# Imports
import random
import ast

def welcome_to_the_game():
    name = input("What's your name?: ")
    print("\nHello, " + name + "!")
    return name # In case I need it for further implementations

def generate_hidden_number():
    upper_range = check_type(input("Enter upper range: "))
    while upper_range <= 20:
        upper_range = input("\nThat seems a bit too easy, it should probably be over 20! Try again: ")
        upper_range = check_type(upper_range)
    print("\nGood! I'll be thinking of a number between 1 and", upper_range)
    hidden_number = random.randint(1, upper_range)
    return hidden_number

def decide_my_max_guesses(hidden_number):
    my_max_guesses = check_type(input("Enter max number of guesses: "))
    return my_max_guesses

def print_hint_string(my_guess, hidden_number):        
        guess_dif = hidden_number - my_guess
        if guess_dif < -20 or guess_dif > 20: # How far off?
            hint = " way "
        elif guess_dif < -10 or guess_dif > 10:
            hint = " "
        elif guess_dif < -4 or guess_dif > 4:
            hint = " a little bit "
        elif guess_dif < -1 or guess_dif > 1:
            hint = " just a little bit "
        elif guess_dif == -1 or guess_dif == 1:
            hint = " so close! just a little bit "
        if my_guess > hidden_number: # Too high or too low?
            direction = "lower."
        else:
            direction = "higher."
        print("\nThat is not correct. My number is", hint, direction, sep="")

def game_over_or_win(my_max_guesses,my_used_guesses, hidden_number):
    if my_used_guesses >= my_max_guesses:
        print("\nYou are out of guesses, the correct number was " + str(hidden_number) + ".")
    else:
        print("\nThat's right! I was thinking of " + str(hidden_number) + "!")

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
    print("\nI'm going to think of a number and your are going to guess it. What range do you think is reasonable? 1 to what?")
    hidden_number = generate_hidden_number()
    print("\nHow many guesses do you need?")
    my_max_guesses = decide_my_max_guesses(hidden_number)
    my_used_guesses = 0
    my_guess = input("\nWhat number am I thinking of?: ")
    while str(my_guess) != str(hidden_number):
        my_guess = check_type(my_guess)
        hint_string = print_hint_string(my_guess, hidden_number)
        my_used_guesses += 1
        if my_used_guesses == my_max_guesses:
            break
        if my_used_guesses == my_max_guesses - 1:
            print("only", my_max_guesses - my_used_guesses, "guess left...")
        else:
            print(my_max_guesses - my_used_guesses, "guesses left")
        my_guess = input("\nTry again: ")
    game_over_or_win(my_max_guesses, my_used_guesses, hidden_number)

if __name__ == "__main__":
    main()