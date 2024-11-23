import os

while True:

    PIN = os.environ.get("pin")

    auth = input("Enter the pin: ")

    if auth == PIN:
        account = float(input("how much is in your account: € "))
        account = round(account, 2)

        Dynamic_variable = "IBAN"

        vars()[Dynamic_variable] = input("Enter Irish IBAN to send money to:  ")
        length = len(vars()[Dynamic_variable])

        if length != 22 or IBAN[0:1] == "IE":
            print("SOMETHING WRONG WITH IBAN \nTRY AGAIN")
            vars()[Dynamic_variable] = input("Enter IRISH IBAN to send money to:  ")


        money = float(input(F"enter how much money your sending to {IBAN}: €"))
        money = round(money, 2)

        print(F"Sending €{money} to {IBAN} ......")

        sum = account - money

        print(F"BALANCE: €{sum}")

    if auth != PIN:
        print("wrong pin! Try again")
        auth = input("Enter the pin: ")



        

   