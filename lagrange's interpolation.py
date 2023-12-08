# Lagrange's Interpolation
# by: Shoumik Acharya

# Data for interpolation
X = [float(x) for x in input("Enter X's(space separated): ").split()]
Y = [float(y) for y in input("Enter Y's(space separated): ").split()]

if len(X) is not len(Y):
    print("not equal data.")
    exit()
if len(X) <= 2:
    print("not sufficient data.")
    exit()

x = float(input("\nEnter x for which y has to be computed: "))
l = []

for i in range(len(X)):
    numerator, denominator = 1, 1
    for j in range(len(X)):
        if j == i:
            continue
        numerator *= x - X[j]
        denominator *= X[i] - X[j]
    l.append(numerator / denominator)

print("\ncomputed results: ")
res = 0
for i in range(len(l)):
    print(f"l{i} = {l[i]}")
    res += l[i] * Y[i]
print(f"\ny({x}) = {res}")
