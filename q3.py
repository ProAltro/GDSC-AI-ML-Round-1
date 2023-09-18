n = int(input("Enter order of the square matrix: "))

m1, m2 = [], []

for i in range(n):
    m1.append(
        list(
            map(
                int,
                input(f"Enter elements of {n+1} row of the first matrix: ").split(" "),
            )
        )
    )

for i in range(n):
    m2.append(
        list(
            map(
                int,
                input(f"Enter elements of {n+1} row of the second matrix: ").split(" "),
            )
        )
    )


trace = 0
for i in range(n):
    for j in range(n):
        trace += m1[i][j] * m2[j][i]

print(f"Trace of the matrix is {trace}")
