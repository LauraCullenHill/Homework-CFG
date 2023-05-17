"""
A] Write a function that returns the N

th number in the following sequence

8, 15, 22, 29, 36, ...
For example:
● num_in_seq(1) = 8
● num_in_seq(5) = 36
● num_in_seq(10) = 71
"""

# The sequence are multiples of 7 plus one each number.
def num_in_sequence(n):
    #base case
    if n == 1:
        return 8
    else:
        return num_in_sequence(n - 1) + 7


# test this with examples
print(num_in_sequence(1))
print(num_in_sequence(5))
print(num_in_sequence(10))

