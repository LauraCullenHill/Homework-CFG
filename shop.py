my_basket = {"apple": 0.50, "persian cat": 800, "orange": 0.50}

budget = 1000


def basket_total(basket):
    basket = sum(basket.values())
    return basket


def if_exit():
    exit = (input("Do you wish to exit? y/n "))
    if exit == 'n':
        print(f"Please pay {total}")
    else:
        print("You are now leaving checkout...")
        quit()



# def exception_counter(Exception):
#     counter = 0


total = basket_total(my_basket)
my_list = list(my_basket.keys())
items = ', '.join(my_list)
print(f"Welcome to the store \nYour total comes to: £{total}")

try:
    if_exit()
    if budget <= basket_total(my_basket):
        raise Exception
except:
    print("You do not have enough money")
else:
    print("You have enough money, payment accepted")
    success = True
    print("Please take your " + items)
finally:
    print('Program finished')
