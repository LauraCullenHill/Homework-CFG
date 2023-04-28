def can_pay(price, cash_given):
   if type(price) != int or type(cash_given) != int:
       raise ValueError("price and cash_given must be integers.")
   if cash_given >= price:
        return True
   else:
       return False

testinggggg
