# TASK 1

# Question 1

# sunny = input('Is it sunny today? y/n: ')

# if sunny == 'y':
#     print('Take your sunglasses')
# else:
#     print("You don't need sunglasses")

# Question 2

# my_money = int(input('How much money do you have? '))
# hours = int(input('How many hours do you need the venue for? '))
# venue_cost = (200 * hours * 1.1)
#
# if my_money >= venue_cost:
#     print('You can afford the venue')
# else:
#     print('You cannot afford the venue')


# Question 3

# def print_word():
#     num = (input("What is your number: "))
#
#     digit = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight',
#              '9': 'Nine'}
#     if len(num) == 1:
#         print("Zero Tens, " + digit[num[0]] + " Ones")
#     else:
#         print(digit[num[0]] + " Tens, " + digit[num[1]] + " Ones")
#
# print_word()


#TASK 2


#Question 1

# students = ["Chloe", "Anna", "Lauren", "Shreya", "Siobhan"]
# print(sorted(students)[0])


#Question 2

# shop = {
#     "book": "1.20",
#     "lamp": "7.50",
#     "table": "25.00",
#     "brush": "3.00",
# }
#
# def price_of_item():
#     item = (input('What item do you want? '))
#     if item in shop:
#         print("this item is £" + shop[item])
#     else:
#         print("We do not have this item")
#
# price_of_item()


#Question 3

# import random
#
# def calc_probability(num):
#     count = 0
#     for i in range(1, 7):
#         for j in range(1, 7):
#             if i + j == num:
#                 count += 1
#     probability = count / 36.0
#     return probability
#
# user_input = int(input("You have two dice. \nWhat sum of the numbers are you trying to get? "))
# probability = round(((calc_probability(user_input)) *100), 2)
# print(f"The probability of getting the number {user_input} is {probability}%")


# TASK 3

file = open('./song.txt', 'r')

content = file.read()


for line in file:
    if 'sing' in line:
        print(line)






# TASK 4