#odd or even
def check_odd_even(number):
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")

check_odd_even(12)
check_odd_even(5)



#count vowels
def count_vowels(text):
    count = 0

    for characters in text.lower():
        if characters in "aeiou":
            count+=1

    return count

result = count_vowels("Tony Stark")
print("Number of vowels: ", result)


#check prime
def check_prime(num):
    if num <= 1:
        print(num, "is not prime")
        return

    for i in range(2, num):
        if num % i == 0:
            print(num, "is not prime")
            return

    print(num, "is prime")

check_prime(7)