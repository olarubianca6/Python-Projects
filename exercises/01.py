import math

# Write a program which will find all such numbers
# which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence
# on a single line.

numbers = []

for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        numbers.append(i)

print(numbers)


# Write a program which can compute the factorial of a given numbers.


def get_factorial(x):
    fact = 1
    if x < 0:
        print('please provide a positive nr')
    else:
        for i in range(1, x + 1):
            fact = fact * i
        print(fact)


get_factorial(8)


# With a given integral number n, write a program to generate
# a dictionary that contains (i, i*i) such that is an integral number
# between 1 and n (both included). and then the program should print
# the dictionary.


def print_dict(n):
    di = {}
    for i in range(1, n + 1):
        di[i] = i * i
    print(di)


print_dict(8)

# Write a program that calculates and prints the value
# according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input
# to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated
# input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24


def get_sequence(d):
    numbers = [x for x in d.split(',')]
    c = 50
    h = 30
    seq = []
    for n in numbers:
        q = round(math.sqrt((2 * c * float(n)) / h))
        seq.append(q)
    print(seq)


get_sequence("100,150,180")
