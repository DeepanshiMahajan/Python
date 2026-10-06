#without function

price = 100
new_price = price + 0.18 * price
print(new_price)


#with function
def add_gst(price):
    new_price = price + 0.18 * price
    print(new_price)

add_gst(200)

#multiple parameters
def sum(num1, num2):
    print(num1 + num2)

sum(10, 40)