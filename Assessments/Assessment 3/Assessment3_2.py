"""
2.1 A) Write a function that takes in a string and returns the number of
unique consonants [10 marks]
EXAMPLE INPUT: “cat”
EXAMPLE OUTPUT: 2 (‘c’ and ‘t’ are both unique)
EXAMPLE INPUT: “cataract”
EXAMPLE OUTPUT: 1 (‘r’ is the only unique consonant)
"""


def num_unique_consonants(input_string):

    # define vowels (easier than consonants)
    vowels = ['a', 'e', 'i', 'o', 'u']

    # Remove all spaces
    string = input_string.replace(" ", "")
    # (make lower case, remove punctuation, remove anything that is not a letter)

    # create empty list
    uniq_cons = []

    # iterate through the characters
    for char in string:
        if char in uniq_cons:
            # remove any duplicates
            uniq_cons.remove(char)
        # make sure the character is a consonant and not a vowel or already there
        elif char not in vowels and char not in uniq_cons:
            # add to the list
            uniq_cons.append(char)

    # get the number of items in the list
    result = len(uniq_cons)
    print(result)


# cat test
num_unique_consonants("i am a cat called hector")


"""
B) What is the time and space complexity of your solution?
If you are making any assumptions in your calculations, list them.
[2 marks]
"""

# O(n^2) time complexity

# O(n) space complexity

"""
2.2 Write a function that finds how many squares are in a X by X grid.
For example a 2x2 Grid has 5 squares as shown below:
"""

# x * x + previous number of squares = new number of squares


def squares_in_grid(x):
    if x == 1:
        return 1
    else:
        return (x * x) + (squares_in_grid(x-1))

sresult = squares_in_grid(3)
print(sresult)
