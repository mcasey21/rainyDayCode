
def pizza_order(size, *args):
    print(F"Your Pizza order is:\n {size}")
    print(F"Toppings: \n {args}\n")


pizza_order("small", "pepporoni", "meatballs", "bacon", "ham")
