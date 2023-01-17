import re

def enter_password_for_evaluation():
    password = input("Enter your password to get it rated!: ")
    print("the password entered is '" + password + "'? ... Let's figure out if it's any good!")
    return password

def scoring_password(password):
    content_checks = ['[0-9]', '[A-Z]', '[a-z]', '[$&+,:;=?@#|\'<>.^*()%!-]']
    passed = 0
    # score on content
    for check in content_checks:
        match = re.search(check, password)
        if match:
            passed += 1
    score = passed
    
    # score on length (also takes content into account)
    if passed == 4:
        score = score + len(password) / 4
    elif passed == 3:
        score = score + len(password) / 5
    else:
        score = score + len(password) / 8
    # score limit
    if score > 10:
        score = 10
    return score

def print_verdict(score):
    verdict = ['not even a password!', 'really bad!', 'just bad!', 'actually bad!', 'pretty bad!', 'so so.', 'pretty ok!', 'pretty good', 'actually really good!','a fantastic password!', 'PERFECT! I love it!']
    print("it's " + verdict[int(score)] + " I'd rate it " + str(int(score)) + "/10!")

def main():
    password = enter_password_for_evaluation()
    score = scoring_password(password)
    print_verdict(score)

if __name__ == "__main__":
    main()