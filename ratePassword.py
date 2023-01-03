# Hello and big thanks for using your precious time to check my shitty code!

# I rearranged the whole file based on an article link to me by a firend:
# https://realpython.com/python-main-function/#best-practices-for-python-main-functions
# It's regarding best practices and I though it would be a good idea to practice the best
# practices :)

# Another friend suggested giving functions much more specific names, even if they are
# up to 4-5 words long.

# I did notice sending the previous version of the code to multiple people that only very
# few of them had any specific feedback on the code itself and I refuse to believe it's 
# near flawless so from now on I intend to put comments with questions in my code where 
# I feel it's lacking and ask for specific feedback on these points

############################################################################################

# I took from the mention best practices article that I should do import in the top of
# the file? Please confirm or let me know when this may not be appropriate
import re

def enterPasswordForEvaluation():
    password = input("Enter your password to get it rated!: ")
    print("the password entered is '" + password + "'? ... Let's figure out if it's any good!")
    return password

def scoringPasswordOnContent(password, score, passed):
    contentChecks = ['[0-9]', '[A-Z]', '[a-z]', '[$&+,:;=?@#|\'<>.^*()%!-]']
    for check in contentChecks:
        match = re.search(check, password)
        if match:
            passed += 1
            score += 1
    return score, passed

def scoringPasswordOnLength(password, score, passed):
    if passed == 4:
        score = score + len(password) / 4
    elif passed == 3:
        score = score + len(password) / 5
    else:
        score = score + len(password) / 8
    if score > 10:
        score = 10
    return score

def printVerdict(score):
    verdict = ['not even a password!', 'really bad!', 'just bad!', 'actually bad!', 'pretty bad!', 'so so.', 'pretty ok!', 'pretty good', 'actually really good!','a fantastic password!', 'PERFECT! I love it!']
    print("it's " + verdict[int(score)] + " I'd rate it " + str(int(score)) + "/10!")

# Best practices said that even though Python does not have a main() it's good for readability
# for developers of other languages since this is the case in C and Java among others.
# Are there any downsides to this?
def main():
    # Define variables
    score = 0
    passed = 0
    # Run through the functions
    password = enterPasswordForEvaluation()
    contentResult = scoringPasswordOnContent(password, score, passed)
    # Unpacking contentResult (tuple) back into variables
    # Is there a way to return mutiple variables by themselves from the function to remove
    # the need to unpack them afterwards? If there is, is there any good reason to do it
    # that way instead?
    score, passed = contentResult
    score = scoringPasswordOnLength(password, score, passed)
    printVerdict(score)

# Apparently Python has different Execution modes so this little thing at the end makes it
# so that if you run the scrpt on it's own it will run main() but if you import it to another
# file it will not because it will return False. The purpose seems to be that you can then
# import this file to other projects and call a single function rather than the while file.
# Most likely none of these functions would be very usable to other people but might be a 
# good habit to use this approach. Does anyone know of any downsides to this?
if __name__ == "__main__":
    main()