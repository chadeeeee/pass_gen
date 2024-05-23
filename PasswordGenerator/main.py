import string
import random

lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation


def generate(length):
    use_for = lower_case + upper_case + numbers + symbols
    password = "".join(random.sample(use_for, length))
    print("Your password is", password)
