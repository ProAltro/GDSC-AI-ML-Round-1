n = int(input("Enter n: "))

c = 0
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print((c % n) + 1, end=" ")
        c += 1
    print()
