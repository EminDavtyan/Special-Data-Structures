class Node:
    def __init__(self, value) -> None:
        self.value = value 
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first
    
    def enqueue(self, value):
        new_node = Node(value)
        if not self.first:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if not self.first:
            return None
        if self.first == self.last:
            self.last = None
        self.first = self.first.next
        self.length -= 1

    def __repr__(self) -> str:
        temp = self.first
        i = []
        while temp:
            i.append(temp.value)
            temp = temp.next
        return f'{i}'
    

if __name__ == '__main__':        
    q1 = Queue()
    q1.enqueue(10)
    q1.enqueue(20)
    q1.enqueue(30)
    q1.peek()
    q1.dequeue()
    q1.enqueue(100)
    print(q1)