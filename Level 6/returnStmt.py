#returning a value
def add_gst(price):
    new_price = price + 0.18 * price
    return new_price

final_price = add_gst(100)

print("Final Price: ", final_price)



#no parameters
def greet():
    print("Welcome to Python !")

greet()