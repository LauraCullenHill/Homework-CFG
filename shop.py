my_basket = {"item": "apple", "price": 0.50},\
            {"item": "persian cat", "price": 800},\
            {"item": "orange", "price": 0.50},\
            {"item": "banana", "price": 0.50}

budget = 100


def basket_total(basket):
    basket = sum(b["price"] for b in basket.item() if b)
    return basket

# def exception_counter(Exception):
#     counter = 0


def not_in_budget(basket):
    basket_total(basket)
    if budget <= basket_total(basket):
        raise ValueError("You do not have enough money to complete the transaction")
    try_again = input("Do you want to try again? y/n ")
    if try_again == 'y':
        run()
    else:
        success = False


try:
    total = basket_total(my_basket)
    items = my_basket.values()
    print(f"Welcome to the store \nYour total comes to: £{total}")
    exit = (input("Do you wish to exit? y/n "))
    if exit == 'n':
        print(f"Please pay {total}")
    else:
        print("You are now leaving checkout...")
except ValueError:
    not_in_budget()
else:
    print("You have enough money, payment accepted")
    success = True
finally:
    if success:
        print(f'Please take your {items}')
    else:
        print('Unsuccessful')
