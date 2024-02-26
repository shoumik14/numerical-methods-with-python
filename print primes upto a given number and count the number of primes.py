def isPrime(num):
    p=True

    for i in range(2,num):
        if num%i==0:
            p=False
            break
    return p

num=int(input("Enter a number: "))
count=0
print("primes upto ",num,": ")
for i in range(2,num+1):
    if isPrime(i):
        print(i)
        count+=1
print(f"number of primes = {count}")