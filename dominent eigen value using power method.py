import numpy as np

size=int(input("Enter the order of the matrix: "))
A,ch=[],""

for i in range(size):
    for j in range(size):
        temp=float(input(f"enter element a{i+1}{j+1}: "))
        A.append(temp)

A=np.array(A).reshape(size,size)

print(A)
X=[]
print("enter the initial guess vector:")
for i in range(size):
    temp=float(input())
    X.append(temp)
X=np.array(X).reshape(size,1)

while(ch!='n'):
    P=A@X
    l=P[size-1,0]
    print(f"eigen value approximation= {l}")
    X=P*(1/l)
    print("corrosponding eigen vector approximation: ")
    print(X)

    ch=input("another iteration? ")
