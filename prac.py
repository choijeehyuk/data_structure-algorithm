class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def __len__(self):
        return len(self.items)


S = Stack()
S.push(1)
S.push(2)
S.push(4)
print(len(S))
print("안녕안녕안녕")
print("222")
print("333")
print("444")
print("555")
