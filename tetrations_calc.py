print("A tetration is a number where the exponent is on the left")
print("It represents the base number ^ number (repeats as many times as the exponent is)")
print(" ")

small_num = int(input("SMALL NUMBER: ")) # 3 tetrate 2 = 16 = 2^2^2
big_num = int(input("BIG NUMBER: "))

small_num = small_num + big_num

zero = 0

tetrate = big_num**big_num

for i in range(small_num):
    zero = zero + tetrate

print(zero)

a = 3*(3**3)

print(F"{a:_}")


