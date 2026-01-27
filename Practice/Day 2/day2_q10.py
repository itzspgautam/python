N = int(input("Enter number of terms: "))

a, b = 0, 1

for i in range(N):
    print(a, " ")
    a, b = b, a + b
