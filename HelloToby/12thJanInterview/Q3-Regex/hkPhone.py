import re

pattern = "^\+[852]+\s+[\d]{4}\s+[\d]{4}$"

user_input = input()

if(re.search(pattern, user_input)):
    print("Got it right")

else:
    print("nah fam")