#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)

def valid_user_input(user_input):
    if (user_input < 0):
        print("Invalid input, please try again.")
        return False
    else:
        return True

def fibonacci(num_terms):
    sequence = [0]
    next_num = 1
    for i in range(num_terms-1):
        sequence.append(next_num)
        next_num += sequence[i]
    return sequence

def print_sequence(sequence):
    print("The Fibonacci sequence is: ", sequence)

user_input = int(input("How many terms of the Fibonacci Sequence do you want: "))
validity = valid_user_input(user_input)
while (validity == False):
    user_input = int(input("How many terms of the Fibonacci Sequence do you want: "))

sequence = fibonacci(user_input)
print_sequence(sequence)
