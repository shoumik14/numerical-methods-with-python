# print prime numbers between 2 given numbers
# By: Shoumik Acharya

# returns true if the given number is prime
def isPrime(num):
    p = True

    if num <= 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                p = False
                break
        return p


a = int(input("Enter the lower limit: "))
b = int(input("Enter the upper limit: "))

print(f"prime number(s) between {a} and {b}: ")
for i in range(a, b + 1):
    if isPrime(i):
        print(i)