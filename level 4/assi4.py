#1
print("ODD NUMBERS : ")
for i in range(1, 20):
    if i % 2 != 0:
        print(i)

#2
print("Table of 57")
num = 57
for i in range(1, 10):
    print(num * i)

#3
print("multiple of 3 except 15")
for number in range(3, 50, 3):
    if number == 15:
        continue
    print(number)