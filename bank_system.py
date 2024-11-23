import random as r


start_up = int(input("Login(1) or Sign-Up(2): "))

if start_up == 2:
    print("WELCOME TO MC BANKS!")
    account_num = r.randint(1000, 9000)
    print(F"your account number is {account_num}")
    password = input("enter your password: ")
    print("You must now login")
    start_up == 1


    if password[0] != password[0].upper():
        print("must start with a capital letter: ")
        password = input("enter a valid password: ")
        
    if password[0] == password[0].upper():
        print(F"Account number: {account_num}\nPassword: {password}")


if start_up == 1:
    Login_acc_num = int(input("enter account number: "))
    Login_pw = input("enter password: ")

    if Login_acc_num != account_num and Login_pw != password:
        print("YOUR DETAILS ARE WRONG \nTRY AGAIN!")
        Login_acc_num = int(input("enter account number: "))
        Login_pw = input("enter password: ")

    if Login_acc_num == account_num and Login_pw == password:
        print("WELCOME!")
        services = int(input("which service would you like: \n Transfer(1) \n Check Balance(2) \n Card details(3) \n enter here:"))
    
    
    
    
