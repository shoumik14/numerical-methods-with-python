a = int(input("enter a number:"))

for i in range(2, ((a // 2) + 1)):
    if a % i == 0:
        print("not prime, divisible by: ", i)
        quit()
print("number is prime")