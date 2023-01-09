# imports
import random
import ast

def welcome_to_the_game():
    name = input("What's your name?: ")
    print("\nHello, " + name + "!\n")
    print("I'm thinking of a number between 1 and 100, you have 7 chances to guess it")
    return name # In case I need it for further implementations

def guessing_away(hidden_number):
    my_max_guesses = 7 # I might make an option for this but will keep "7" for now
    my_used_guesses = 0
    my_guess = input("What number am I thinking of?: ")

    while str(my_guess) != str(hidden_number):
        try: # set type of my_guess based on input (default string)
            my_guess = ast.literal_eval(my_guess)
        except (ValueError, SyntaxError):
            pass
        
        if type(my_guess) == float: # Giving hints based on wrong type input
            print("\nI'll give you a hint! My number does not have any decimals!")
        elif type(my_guess) == str:
            print("\nMy number is actually a number, you don't need to waste guesses on other things!")
        else: # Generating a hint from a valid guess
            guess_dif = hidden_number - my_guess
            if guess_dif < -25 or guess_dif > 25: # how far off?
                hint = " way "
            elif guess_dif < -15 or guess_dif > 10:
                hint = " "
            elif guess_dif < -5 or guess_dif > 5:
                hint = " a little "
            elif guess_dif <= -1 or guess_dif >= 1:
                hint = " just a little bit "
            if my_guess > hidden_number: # too high or too low?
                direction = "lower."
            else:
                direction = "higher."

            # Give hint on wrong (but correct type) guess
            print("\nThat is not correct. My number is", hint, direction, sep="")

        my_used_guesses += 1
        if my_used_guesses == my_max_guesses:
            break

        if my_used_guesses == 6:
            print("only", my_max_guesses - my_used_guesses, "guess left...")
        else:
            print(my_max_guesses - my_used_guesses, "guesses left")

        my_guess = input("\nTry again: ")

    return my_used_guesses

def game_over_or_win(my_used_guesses, hidden_number):
    if my_used_guesses >= 7: # will change "7" to variable if I make an option for range
        print("\nYou are out of guesses, the correct number was " + str(hidden_number) + ".")
    else:
        print("\nThat's right! I was thinking of " + str(hidden_number) + "!")

def main():
    hidden_number = random.randint(1,100) # I might make options of range but until then I will just define it here
    name = welcome_to_the_game()
    my_used_guesses = guessing_away(hidden_number)
    game_over_or_win(my_used_guesses, hidden_number)

if __name__ == "__main__":
    main()