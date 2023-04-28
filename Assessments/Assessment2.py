# ASSESSMENT 2
# Section 2: Concept Questions

#2.1
# Write a function that takes in an input and checks to see if it’s an isogram. The function should return True or False.

def is_isogram():
    try:
    # get an input
        string = input("Please enter a word to see if it is an isogram: ")
    # cannot be blank or number. I think input makes it a string though so it cant be an integer or list?
    except ValueError as ve:
        print(ve)
    else:
        # get all letters from the string
        letters = []
        for letter in string:
            letters.append(letter)
            if letter in letters:
                return False
        else:
            return True


#for 2.2 see test_isogram file. copied below for ref:
# from unittest import TestCase, mock, main
# from Assessment2 import is_isogram
#
#
# class TestIsIsogram():
#
# #testing to see if an isogram returns true
#     def test_1(self):
#         string = "abcdefg"
#         expected = True
#         actual = is_isogram(string)
#         self.assetEqual(actual, expected)
#
#
# #testing to see if a string that is not an isogram returns false
#     def test_1(self):
#         string = "abcdefgabc"
#         expected = False
#         actual = is_isogram(string)
#         self.assetEqual(actual, expected)
#
# #an empty string should return false
#     def test_1(self):
#         string = ""
#         expected = False
#         actual = is_isogram(string)
#         self.assetEqual(actual, expected)
#
#
# TestIsIsogram()
#




# Section 3: Python Challenge

# You are tasked with calculating the minimum classes we need to have so we know how many people to employ. Write a function which when
# given a number of students, calculates and prints out a string for your proposed number of classes, and a dictionary showing the allocation.
#
# Key Constraints:
# The maximum size of a class is 30
# There needs to be a minimum of 2 classes
# The distribution of each class should be as even as possible.
# We want to hire as little people as possible - so where possible focus on bigger classes, and less of them!



#define the function
def num_of_classes(students):
    #define edge cases
    if students < 60:
        raise Exception("There must be more than 60 students to allow us to have at least 2 classes")
    if students < 0:
        raise ValueError("Cannot be a negative number of students")
    if not students == ():
        # divide students by 30. round up to whole number so we know how many classes/ instructors we need.
        base_classes = students / 30

        allocation = []
        # if there are under 30 students in a list then carry on adding a student.
        while students in allocation <= 30:
            # adding students to each class so the students are divided equally between the classes.
            # unsure but something with a loop in a loop where it appends to each list. number of lists is determined by base_classes.
            for i in students:
                for j in range(base_classes):
                    # create the base_classes number of dictionaries
                    return allocation.append(len(students))  # we need the number of students in each class not the list of them

        print({f"class {base_classes + 1}: " + allocation})  # need to add one each time we start a new class number for the output the follow with the list

num_of_classes(100)
