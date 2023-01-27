# Slot machine project based on: 
# https://www.youtube.com/watch?v=th4OBktqK1I
#
# The goal is to make a similar project but improve parts where
# I see a better or less repetative solution

# Imports and constants
MAX_DEPOSIT = 1000
MIN_DEPOSIT = 1
STR_DEPOSIT = f"How much do you want to deposit? ({MIN_DEPOSIT}-{MAX_DEPOSIT}) \nDeposit $"
MAX_LINES = 3
MIN_LINES = 1
STR_LINES = f"How many lines do you want to bet on? ({MIN_LINES}-{MAX_LINES}) \nLines #"
MAX_BET = 100
MIN_BET = 1
STR_BET = f"How much do you want to bet? ({MIN_BET}-{MAX_BET}) \nBet $"

# Get inputs during the game
def get_deposit():
    amount = get_number(STR_DEPOSIT, MAX_DEPOSIT, MIN_DEPOSIT)
    return amount
    
def get_lines():
    lines = get_number(STR_LINES, MAX_LINES, MIN_LINES)
    return lines

def get_bet():
    bet = get_number(STR_BET, MAX_BET, MIN_BET)
    return bet 

# Check inputs
def get_number(string, max_num, min_num):
    while True:
        number = input(string)
        if number.isdigit():
            number = int(number) 
            if min_num <= number <= max_num:
                break 
            else:
                print("Enter a valid number.")
        else:
            print("Please enter a number.")

    return number

def main():
    amount = get_deposit()
    lines = get_lines()
    bet = get_bet()
    print(amount, lines, bet)

if __name__ == "__main__":
    main()
