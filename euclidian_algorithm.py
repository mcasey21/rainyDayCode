# a = q(b) + r

num1 = int(input("Enter first number:  "))
num2 = int(input("Enter second number:  "))

r_list = []


if num1 > num2:
    a = num1
    b = num2
else:
    a = num2
    b = num1

q = a//b
r = a - (q*b)

r_list.append(r)

print(F"{a} = {q}({b}) + {r}")

while r != 0:
    if r != 0:
        a = b
        b = r
    
    q = a//b
    r = a - (q*b)

    r_list.append(r)

    print(F"{a} = {q}({b}) + {r}")

if r == 0:
    print(F"GCD: {r_list[-2]}")
