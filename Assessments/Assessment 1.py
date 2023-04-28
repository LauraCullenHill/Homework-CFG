#question 2.1
#
# students = ["Ana", "beth", "CHARLIE"]  # keep this line
#
# formatted_students = []
#
# for student in students:
#     formatted_students.append(student.lower())
#
#
# print(formatted_students)

# students = ["Ana", "beth", "CHARLIE"]
#
# formatted_students = [students.lower(" ") for name in students]
#
# print(formatted_students)


#question 2.2

# input_str = 'practice'
# ans_1= input_str[-4:-9:-2]
# print(ans_1)

#question 2.3
#
# filename = input("Enter the name of the text file: ")
#
# def file_read():
#     with open('file', 'r''w') as f:
#         for line in file:
#             words = line.strip().split()
#
# file_read('name of file here')

#question 2.4

# items = {
#      "apple": 1.20,
#      "cake": 7.50,
#      "orange": 2.00,
#      "pizza": 6.00
# }
#
# def total():
#      total_cost = sum(items.values())
#      print(f"The total is: £{total_cost}")
#
#
# total()

#question 3

from datetime import datetime, timedelta

def add_date():
    date = input('Please enter the date in the following format DD/MM/YYYY')
    date_obj = datetime.strptime(date, '%d/%m/%Y')
    day_add = int(input('Please enter how many days you wish to add: '))
    output = date_obj + timedelta(days=day_add)
    new_date_formatted = output.strftime('%d/%m/%Y')

    print(f'The resultant date is {new_date_formatted} ')


def compare_date():
    date_a = input('Please enter the first date in the following format DD/MM/YYYY')
    da = datetime.strptime(date_a, '%d/%m/%Y')
    date_b = input('Please enter the first date in the following format DD/MM/YYYY')
    db = datetime.strptime(date_b, '%d/%m/%Y')
    delta = da - db
    print(f'There are {delta.days} days between the given dates')


def add_compare():
    task = input('Please select one of the following: add or compare')
    if task == 'add':
        add_date()
    elif task == 'compare':
        compare_date()

add_compare()








