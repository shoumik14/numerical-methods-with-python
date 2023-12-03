import numpy as np

size=int(input("Enter the order of the matrix: "))
A,ch=[],""

for i in range(size):
    for j in range(size):
        temp=float(input(f"enter element a{i+1}{j+1}: "))
        A.append(temp)

A=np.array(A).reshape(size,size)

print(A)

if not np.array_equal(A,np.transpose(A)):
    print("not symmetric")
    exit()

while ch!='n':
    non_diagonal_elements=[]
    for i in range(size):
        for j in range(size):
            if i<j:
                non_diagonal_elements.append((abs(A[i,j]),i,j))

    maximum=max(non_diagonal_elements)
    print(f"largest non-diagonal element is (along with row and column number) {maximum}")
    I,J=maximum[1],maximum[2]

    if A[I,I]==A[J,J] and A[I,J]>0:
        theta=round(np.pi/4,4)
    elif A[I,I]==A[J,J] and A[I,J]<0:
        theta=round(-np.pi/4,4)
    else:
        theta=round(0.5*np.arctan((2*A[I,J])/(A[I,I]-A[J,J])),4)
    print(f"rotation angle is {theta}")

    #constructing the P matrix
    P=np.full((size,size),float(0))
    for i in range(size):
        for j in range(size):
            if i==j and j!=I and j!=J:
                P[i,j]=1
            elif i==j==I or i==j==J:
                P[i,j]=round(np.cos(theta),4)
            elif i==I and j==J:
                P[i,j]=round(-np.sin(theta),4)
            elif i==J and j==I:
                P[i,j]=round(np.sin(theta),4)
            else:
                P[i,j]=0

    print("The P matrix is, ")
    print(P)

    A=np.transpose(P)@A@P
    A=A.round(4)
    print(A)

    ch=input("another iteration? ")

print("The eigen values are: ")
for i in range(size):
    print(A[i,i])
