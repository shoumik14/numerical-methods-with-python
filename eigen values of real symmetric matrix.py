import numpy as np

size=int(input("Enter the order of the matrix: "))
A,ch,p_matrices=[],"",[]

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
        theta=np.pi/4
    elif A[I,I]==A[J,J] and A[I,J]<0:
        theta=-np.pi/4
    else:
        theta=0.5*np.arctan((2*A[I,J])/(A[I,I]-A[J,J]))
    print(f"rotation angle is {theta}")

    #constructing the P matrix
    P=np.full((size,size),float(0))
    for i in range(size):
        for j in range(size):
            if i==j and j!=I and j!=J:
                P[i,j]=1
            elif i==j==I or i==j==J:
                P[i,j]=np.cos(theta)
            elif i==I and j==J:
                P[i,j]=-np.sin(theta)
            elif i==J and j==I:
                P[i,j]=np.sin(theta)
            else:
                P[i,j]=0

    print("The P matrix is, ")
    print(P)
    p_matrices.append(P)

    A=np.transpose(P)@A@P
    print(A)

    ch=input("another iteration? ")

print("The eigen values are: ")
for i in range(size):
    print(A[i,i])

eigen_vectors=np.identity(size)

for X in p_matrices:
    eigen_vectors=eigen_vectors@X
print("And eigen vectors are the columns of the matrix given below, respectively: ")
print(eigen_vectors)
