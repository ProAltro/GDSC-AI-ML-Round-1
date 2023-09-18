t = int(input("Enter the number of test cases: "))


for i in range(t):
    s1 = input("Enter the first string: ")
    s2 = input("Enter the second string: ")
    for i in s1:
        if i in s2:
            print("Yes")
            break
    else:
        print("No")
