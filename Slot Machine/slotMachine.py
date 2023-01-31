# Slot machine project based on: 
# https://www.youtube.com/watch?v=th4OBktqK1I
#
# The goal is to make a similar project but improve parts where
# I see a better or less repetative solution

# Imports and constants
import random

MAX_DEPOSIT = 1000
MIN_DEPOSIT = 1
STR_DEPOSIT = f"How much do you want to deposit? ({MIN_DEPOSIT}-{MAX_DEPOSIT}) \nDeposit $"
MAX_LINES = 3
MIN_LINES = 1
STR_LINES = f"How many lines do you want to bet on? ({MIN_LINES}-{MAX_LINES}) \nLines #"
MAX_BET = 100
MIN_BET = 1
STR_BET = f"How much do you want to bet per line? ({MIN_BET}-{MAX_BET}) \nBet $"

ROWS = 3
COLS = 3

symbol_count= {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_sybmols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_sybmols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_sybmols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
        
    return columns

def print_slot_machine(columns):
    print()
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row])

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

def spin(balance):
    lines = get_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You don't have enough money that that bet, balance is: ${balance}")
        else:
            break
    
    print(f"You are betting ${bet} on {lines} lines. Total bet is ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = get_deposit()
    while True:
        print(f"Current balanve is ${balance}")
        answer = input("\nPress enter to play (type q to quit): ")
        if answer == "q":
            break
        balance += spin(balance)
    
    print(f"You left with ${balance}")

if __name__ == "__main__":
    main()
