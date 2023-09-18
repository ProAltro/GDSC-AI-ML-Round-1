n = int(input("Enter number of test cases: "))


def shortest(s):
    if not s:
        return 0
    if s[0] == s[-1]:
        return len(s)
    return shortest(s[1:-1])


for i in range(n):
    f = input("Enter the final number: ")
    print(shortest(f))
