import tkinter as tk
import math

root = tk.Tk()

#window propeties
root.title("CALCULATOR")
root.configure(background="black")
root.geometry("400x600+450+50") #dimesions of window X x Y, moving window + x + y

#function to enter numbers on screen
def enter_number(num):
    current = screen.get()
    screen.delete(0, tk.END)
    screen.insert(tk.END, current + str(num))

# Create an entry widget to serve as the screen
screen = tk.Entry(root, font=("Arial", 24), justify='right', bg="light grey")
screen.place(x=0, y=0, height=95, width=400)

#func for AC button
def clear_screen():
    screen.delete(0, tk.END)

#func for C button
def clear_recent():
    length = len(screen.get()) #gets current length of screen digits
    recent = length - 1 #minus 1 to get recent digit 
    screen.delete(recent, tk.END)


def Equal():
    expression = screen.get()
    # Replace the custom symbols with valid Python operators
    expression = expression.replace("x", "*").replace("÷", "/")

    

    try:
        result = str(eval(expression))  # Evaluate the expression
        screen.delete(0, tk.END)
        screen.insert(tk.END, result)  # Display the result
    except Exception as e:
        screen.delete(0, tk.END)
        screen.insert(tk.END, "Error")  # Display "Error" in case of invalid expression

#ROW One

#Button AC
buttonAC = tk.Button(root, text="AC", bg="orange", command=clear_screen)
buttonAC.place(x=0, y=95, height=100, width=100)

#Button C
buttonC = tk.Button(root, text="C", bg="grey", command=clear_recent)
buttonC.place(x=100, y=95, height=100, width=100)

#Button SqRT
buttonSqrt = tk.Button(root, text="√", bg="grey", command=lambda: enter_number("√"))
buttonSqrt.place(x=200, y=95, height=100, width=100)

#Button percent
buttonPercent = tk.Button(root, text="%", bg="grey", command=lambda: enter_number("%"))
buttonPercent.place(x=300, y=95, height=100, width=100)


#ROW Two

#Button 7
button7 = tk.Button(root, text="7", bg="white", command=lambda: enter_number(7))
button7.place(x=0, y=195, height=100, width=100)


#Button 8
button8 = tk.Button(root, text="8", bg="white", command=lambda: enter_number(8))
button8.place(x=100, y=195, height=100, width=100)

#Button 9
button9 = tk.Button(root, text="9", bg="white", command=lambda: enter_number(9))
button9.place(x=200, y=195, height=100, width=100)

#Button divide
buttonDivide = tk.Button(root, text="÷", bg="grey", command=lambda: enter_number("÷"))
buttonDivide.place(x=300, y=195, height=100, width=100)


#ROW Three

#Button 4
button4 = tk.Button(root, text="4", bg="white", command=lambda: enter_number(4))
button4.place(x=0, y=295, height=100, width=100)

#Button 5
button5 = tk.Button(root, text="5", bg="white", command=lambda: enter_number(5))
button5.place(x=100, y=295, height=100, width=100)

#Button 6
button6 = tk.Button(root, text="6", bg="white", command=lambda: enter_number(6))
button6.place(x=200, y=295, height=100, width=100)

#Button multiply
buttonMultiply = tk.Button(root, text="x", bg="grey", command=lambda: enter_number("x"))
buttonMultiply.place(x=300, y=295, height=100, width=100)


#ROW four

#Button 1
button1 = tk.Button(root, text="1", bg="white", command=lambda: enter_number(1))
button1.place(x=0, y=395, height=100, width=100)

#Button 2
button2 = tk.Button(root, text="2", bg="white", command=lambda: enter_number(2))
button2.place(x=100, y=395, height=100, width=100)

#Button 3
button3 = tk.Button(root, text="3", bg="white", command=lambda: enter_number(3))
button3.place(x=200, y=395, height=100, width=100)

#Button subtract
buttonSubtract = tk.Button(root, text="-", bg="grey", command=lambda: enter_number("-"))
buttonSubtract.place(x=300, y=395, height=100, width=100)


#ROW five

#Button 0
button0 = tk.Button(root, text="0", bg="white", command=lambda: enter_number(0))
button0.place(x=0, y=495, height=100, width=100)

#Button DP
buttonDP = tk.Button(root, text=".", bg="white", command=lambda: enter_number("."))
buttonDP.place(x=100, y=495, height=100, width=100)

#Button equal
buttonEqual = tk.Button(root, text="=", bg="grey", command=Equal)
buttonEqual.place(x=200, y=495, height=100, width=100)

#Button add
buttonAdd = tk.Button(root, text="+", bg="grey", command=lambda: enter_number("+"))
buttonAdd.place(x=300, y=495, height=100, width=100)


root.mainloop()