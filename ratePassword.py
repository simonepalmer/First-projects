#Imports & definitions
import re
score = 0
passed = 0

#Entering the password you want rated
password = input("Enter your password to get it rated!: ")
print("the password entered is '" + password + "'? ... Let's figure out if it's any good!")

#Scoring your password based on it's contents
def scoring(checks, password, score, passed):
    for check in checks:
        match = re.search(check, password)
        if match:
            passed += 1
            score += 1
    return score, passed

checks = ['[0-9]', '[A-Z]', '[a-z]', '[$&+,:;=?@#|\'<>.^*()%!-]']
results = scoring(checks, password, score, passed)
score, passed = results

#Scoring your password based on it's length
if passed == 4:
    score = score + len(password) / 4
elif passed == 3:
    score = score + len(password) / 5
else:
    score = score + len(password) / 8

#Keeping the score within verdict index
if score > 10:
    score = 10

#Generating the verdict
verdict = ['not even a password!', 'really bad!', 'just bad!', 'actually bad!', 'pretty bad!', 'so so.', 'pretty ok!', 'pretty good', 'actually really good!','a fantastic password!', 'PERFECT! I love it!']
print("it's " + verdict[int(score)] + " I'd rate it " + str(int(score)) + "/10!")