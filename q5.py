class Stack(list):
    def __init__(self):
        super().__init__()

    def push(self, item):
        self.append(item)
        return "pushed successfully"

    def pop(self):
        if len(self):
            return super().pop()
        return "underflow"


stack = Stack()
while True:
    print("1. Push")
    print("2. Pop")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter item to push: ")
        print(stack.push(item))
    elif choice == 2:
        print(stack.pop())
    elif choice == 3:
        i = stack.pop()
        while i != "underflow":
            print(i, end=" ")
            i = stack.pop()
        break
    else:
        print("Invalid choice")
    print()
