from webbot import Browser
import time
import argparse
from random_username.generate import generate_username
import random

# Instantiate the parser
parser = argparse.ArgumentParser(description='Automatically generate protonmail accounts')

# Optional positional argument
parser.add_argument('username', type=str, nargs='?',
                    help='The username of the account')

# Optional positional argument
parser.add_argument('password', type=str, nargs='?',
                    help='The password of the account')

args = parser.parse_args()

if not args.username:
  username = random.choice(generate_username(10))
else:
  username = args.username
 
if not args.password:
  password = "Pr0tonMa1ler"
else:
  password = args.password

web = Browser()
web.go_to('https://account.proton.me/signup?plan=free&billing=12&ref=prctbl&minimumCycle=12&currency=USD&product=mail&language=en')
web.type(username, id='email')
web.type(password, id='password')
web.type(password, id='repeat-password')
web.click('Create account', tag='button')

input("Complete the captcha, then press enter.")

web.close_current_tab()

print("Created protonmail account successfully.\n Username: " + username + "\n Password: " + password)
