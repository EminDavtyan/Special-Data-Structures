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
        '''
        Shows the top item of the Stack
        '''
        return self.top
    
    def push(self, value):
        '''
        Add item to top of Stack
        '''
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
        '''
        Pops top item of the Stack
        '''
        if not self.top:
            return None
        if self.top == self.bottom:
            self.bottom = None
        self.top = self.top.next
        self.length -= 1

    def __repr__(self) -> str:
        temp = self.top
        i = []
        while temp:
            i.append(temp.value)
            temp = temp.next
        return f'{i}'
    

if __name__ == '__main__':        
    s1 = Stack()
    s1.push(1)
    s1.push(2)
    s1.push(3)
    s1.push(20)
    s1.peek()
    s1.pop()
    print(s1)