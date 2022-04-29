

import random

upper_case = "ABCDEFGHIJKLMNOPQRSTUVWZYZ"
lower_case = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
symbols = "@#$%&*!?"
min_pass_length = 10

pass_include = upper_case + lower_case + numbers +symbols

password = "".join(random.sample(pass_include,min_pass_length))

print("Your Password is ",password)