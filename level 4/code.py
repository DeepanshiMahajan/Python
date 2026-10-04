#range
nums = range(5)
print(nums)


# range(start=1, stop=5, step=1)


#while loop
print("Counter using while loop :")
counter = 1
while counter <= 6:
    print(counter)
    counter+=1
print("End")


#for loop
print("Numbers :")
for i in range(1, 6):
    print(i)


print("Even Numbers :")
for i in range(1, 11):
    if i == 10:
        break
    if i % 2 == 0:
        print(i)