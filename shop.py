my_basket = {"apple": 0.50, "persian cat": 800, "orange": 0.50}


# define the functions

def basket_total(basket):
    total = sum(basket.values())
    return total


def my_items(basket):
    my_list = list(basket.keys())
    items = ', '.join(my_list)
    return items


def if_exit():
    exit_process = (input("Do you wish to continue? y/n "))
    if exit_process == 'y':
        print("Please continue.")
    else:
        print("You are now leaving checkout...")
        quit()


def my_budget(basket):
    budget = int(input("How much money do you have?: "))
    if budget >= basket_total(basket):
        return True
    else:
        return False


def in_budget(basket):
    count = 0
    while count < 3:
        if my_budget(basket) >= basket_total(basket):
            return True
        else:
            print("You do not have enough money")
            count += 1
    print("Cannot exceed 3 attempts")
    return False


# define the exceptions

def integer_validation(value):
    if not isinstance(value, int):
        raise ValueError("You must enter an integer")


# run the program with exceptions
def checkout(b):
    total = basket_total(b)
    print(f"Welcome to the store \nYour total comes to: £{total}")
    if_exit()
    in_budget(b)
    if in_budget == True:
        try:
            total = basket_total(b)
            print(f"Please pay £{total}")
        except Exception as exc:
            raise Exception(exc)
        except ValueError as err:
            raise ValueError(err)
        else:
            items = my_items(b)
            print(f"Thank you \nPlease take your {items}")
        finally:
            print('Program finished')
    else:
        print("Exiting checkout")


print(checkout(my_basket))
