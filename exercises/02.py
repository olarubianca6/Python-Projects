import re

# A website requires the users to input username
# and password to register. Write a program to check
# the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated
# passwords and will check them according to the above
# criteria. Passwords that match the criteria are to be
# printed, each separated by a comma.
# Example:
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1


def check_pass():
    accepted = False
    while not accepted:
        password = str(input('Please enter a password: '))
        if len(password) < 6:
            print('Your password needs to be over 6 characters')
        elif len(password) > 12:
            print('Password must be 12 characters or shorter')
        elif not re.search("[#$@]", password):
            print('Password must contain a special character')
        elif not re.search("[a-z]", password):
            print('Password must contain at least one smallcase letter')
        elif not re.search("[A-Z]", password):
            print('Password must contain at least one uppercase letter')
        elif not re.search("[0-9]", password):
            print('Password must contain at least one number')
        else:
            print('You have registered your account successfully')
            accepted = True


check_pass()
