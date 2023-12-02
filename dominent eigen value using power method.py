import numpy as np

size=int(input("Enter the order of the matrix: "))
A,ch=[],""

for i in range(size):
    for j in range(size):
        temp=float(input(f"enter element a{i+1}{j+1}: "))
        A.append(temp)

A=np.array(A).reshape(size,size)

print(A)