"""

    Q3 - REGEX : Checks the validity of the Hong Kong Phone number
    1. Start with a plus sign
    2. Followed by 852 country code
    3. {Optional} One whitespace character
    4. 1 digit from a set of [2,3,5,6,7,9]
    5. 3 digits ranging from 0-9 
    6. {Optional} One more whitespace character
    7. Followed by 4 more digits ranging from 0-9

    Functional Example: +852 5222 0073

"""

# Regex python library for re.search(regex_pattern, respective_input)
import re

# regex_pattern
pattern = "^\+(852)\s*[2,3,5,6,7,9][\d]{3}\s*[\d]{4}$"

#Input from user
print("Please input your HK phone number (+852 XXXX XXXX)")
user_input = input()

while user_input != 'q':


    if(re.search(pattern, user_input)):
        print("Valid Hong Kong Phone Number")
        print("<---------------------->\n")

    else:
        print("Invalid Hong Kong Phone Number")
        print("<-----------XXX----------->\n")

    print("Please input your HK phone number (+852 XXXX XXXX)")
    user_input = input()