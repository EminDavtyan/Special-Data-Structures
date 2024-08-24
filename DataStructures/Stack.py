class Node:
    def __init__(self, value) -> None:
        self.value = value 
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top
    
    def push(self, value):
        new_node = Node(value)
        if not self.top:
            self.top = new_node
            self.bottom = new_node
        else:
            holdingPointer = self.top
            self.top = new_node
            self.top.next = holdingPointer
        self.length += 1

    def pop(self):
        if not self.top:
            return None
        if self.top == self.bottom:
            self.bottom = None
        # holdingPointer = self.top
        self.top = self.top.next
        self.length -= 1

    def __repr__(self) -> str:
        temp = self.top
        i = []
        while temp:
            i.append(temp.value)
            temp = temp.next
        return f'{i}'
    
s1 = Stack()
s1.push(1)
s1.push(2)
s1.push(3)
s1.push(20)
s1.pop()
s1.pop()
s1.pop()
s1.pop()
print(s1)