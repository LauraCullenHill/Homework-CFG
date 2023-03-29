my_basket = {"apple": 0.50, "persian cat": 800, "orange": 0.50}


# define the functions

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
    count = 0
    while count < 3:
        try:
            retry = input("Do you have more money? y/n: ")
            if retry == 'y':
                count += 1
                checkout()
            else:
                count += 1
                break  # exit the inner while loop if the user chooses not to retry
        except:
            if count >= 3:
                print("Cannot exceed 3 attempts")
                break  # exit the outer while loop if the user exceeds 3 retries
    return "End."


# define the exceptions

def in_budget(basket):
    if my_budget() < basket_total(basket):
        raise ValueError("You do not have enough money")


def integer_validation(value):
    if not isinstance(value, int):
        raise ValueError("You must enter an integer")


# run the program with exceptions
def checkout():
    try:
        total = basket_total(my_basket)
        print(f"Welcome to the store \nYour total comes to: £{total}")
        if_exit()
        in_budget(my_basket)
        integer_validation(my_budget())
    except Exception as exc:
        print(exc)
        try_again()
    else:
        total = basket_total(my_basket)
        print(f"Please pay £{total}")
        items = my_items(my_basket)
        print(f"Please take your {items}")
    finally:
        print('Program finished')


checkout()
