#what is in the basket
my_basket = {"apple": 0.50, "persian cat": 800, "orange": 0.50}

#define the functions
def basket_total(basket):
    total = sum(basket.values())
    return total


def if_exit():
    exit_process = (input("Do you wish to exit? y/n "))
    if exit_process == 'n':
        print("Please continue.")
    else:
        print("You are now leaving checkout...")
        quit()


def my_budget():
    budget = int(input("How much money do you have?: "))
    return budget


def my_items(basket):
    my_list = list(basket.keys())
    items = ', '.join(my_list)
    return items


def try_again():
    counter = 0
    retry = input("Do you have more money? y/n: ")
    while retry == 'y' and counter < 3:
        checkout()
        counter += 1
    if counter < 3:
        print("Cannot exceed 3 attempts")
        exit()


# define the exceptions
def in_budget(basket):
    if my_budget() <= basket_total(basket):
        raise ValueError("You do not have enough money")


def integer_validation(basket):
    if not int:
        raise ValueError("You must enter an integer")


# run the program with exceptions
def checkout():
    try:
        total = basket_total(my_basket)
        print(f"Welcome to the store \nYour total comes to: £{total}")
        if_exit()
        in_budget(my_basket)
        integer_validation(my_basket)
    except Exception as exc:
        print(exc)
        try_again()
    else:
        total = basket_total(my_basket)
        print(f"Please pay {total}")
        items = my_items(my_basket)
        print(f"Please take your {items}")
    finally:
        print('Program finished')

checkout()