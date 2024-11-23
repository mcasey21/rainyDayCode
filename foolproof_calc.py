
print("WELCOME TO MY CALCULATOR!")

oper = input("ENTER OPERATOR (+ - x /):  ").lower()

while True:

    if oper == "+":

        try:
            num1 = float(input("FIRST NUMBER:  "))
            num2 = float(input("SECOND NUMBER:  "))
            num3 = num1 + num2
            print(F"{num1} + {num2} = {num3:,}")

        except ValueError:
            print("You didnt enter numbers")

        except Exception:
            print("somthing went wrong!")

        finally:
            again = input("Do you want to go again(y/n):  ").lower()

    elif oper == "-":

        try:
            num1 = float(input("FIRST NUMBER:  "))
            num2 = float(input("SECOND NUMBER:  "))
            num3 = num1 - num2
            print(F"{num1} - {num2} = {num3:,}")

        except ValueError:
            print("You didnt enter numbers")

        except Exception:
            print("somthing went wrong!")

        finally:
            again = input("Do you want to go again(y/n):  ").lower()

    elif oper == "x":

        try:
            num1 = float(input("FIRST NUMBER:  "))
            num2 = float(input("SECOND NUMBER:  "))
            num3 = num1 * num2
            print(F"{num1} x {num2} = {num3:,}")

        except ValueError:
            print("You didnt enter numbers")

        except Exception:
            print("somthing went wrong!")

        finally:
            again = input("Do you want to go again(y/n):  ").lower()

    elif oper == "/":

        try:
            num1 = float(input("FIRST NUMBER:  "))
            num2 = float(input("SECOND NUMBER:  "))
            num3 = num1 / num2
            print(F"{num1} / {num2} = {num3:,}")

        except ValueError:
            print("You didnt enter numbers")

        except Exception:
            print("somthing went wrong!")

        finally:
            again = input("Do you want to go again(y/n):  ").lower()
    else:
        print("you didnt enter an operator!")
        again = input("Do you want to go again(y/n):  ").lower()
        
    if again == "y":
        oper = input("ENTER OPERATOR (+ - x /):  ").lower()

    elif again == "n":
        print("Bye!")
        break
    
    else:
        print("NOT ON OPTION")
        again = input("Do you want to go again(y/n):  ").lower()
