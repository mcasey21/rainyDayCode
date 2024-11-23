
items = []
prices = []

line_length = 30
total_price = 0

while True:
    loop = (input("Add items (y/n): ")).upper()

    if loop == 'Y':

        user_items = input("Enter an item: ")
        user_price = input("Enter price of item: ")
        
        items.append(user_items)
        prices.append(user_price)
    
    else:
        break

"""
- Loop to print receipt
    - Prints all prices in line
    - Adds list items lengths then subtracts line_length
"""

for i in range (len(items)):

    total_length = len(items[i]) + len(prices[i])
    dots = line_length - total_length

    " If the combined item and price length is longer than the line_length, adjust it "
    while dots < 1:
        line_length += 1
        dots = line_length - total_length
        

    print(f"{items[i]} {'.' * dots} {prices[i]}")
    
" Loop to add all prices together "
for price in prices:
    " Cast all the prices to a float "
    total_price += float(price) 
    
" Printing full line of '-' "
dot_line_length = line_length + 2
print("-" * dot_line_length)

" Printing total price at end of ' ' "
space_length = line_length-4
print(f"{' ' * space_length} {total_price}")


