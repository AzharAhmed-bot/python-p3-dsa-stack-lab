class Stack:

    def __init__(self, items = [], limit = 100):
        self.items=items
        self.limit=limit


    def isEmpty(self):
        return len(self.items) == 0
        

    def push(self, item):
        self.items.append(item)

    def pop(self):
        pass

    def peek(self):
        pass
    
    def size(self):
        length=len(self.items)
        return length

    def full(self):
        return len(self.items) == self.limit


    def search(self, target):
        for i in range(len(self.items) - 1, -1, -1):
            if self.items[i] == target:
                return len(self.items) - i - 1
        return -1

    
# stack = Stack()
# stack.push(10)
# stack.push(20)
# stack.push(30)
# stack.push(40)
# stack.push(50)
# print(stack.full())