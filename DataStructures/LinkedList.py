class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self) -> None: 
        '''
        LinkedList {value: any, next:{value: any, next:{...}}}
        '''
        self.head = None
        self.tail = None
        self.length = 0

    def isValid(self, index):
        assert isinstance(index, int), 'Index should be int'
        assert index >= 0, 'Invalid index, negative index'
        assert index <= self.length, f'Index out of range ({self.length})'

    def append(self, value):
        '''
        Append new Node(head node)
        '''
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def prepend(self, value):
        '''
        Prepend new Node(tail node)
        '''
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert(self, index: int, value):
        '''
        Insert new Node[index]
        '''
        self.isValid(index)
        new_node = Node(value)
        i = 0
        pre = self.head
        if index == 0:
            self.prepend(value)
        else:
            while i < index - 1:
                pre = pre.next
                i += 1
            aft = pre.next
            new_node.next = aft
            pre.next = new_node
        self.length += 1

    def remove(self, index: int):
        '''
        Remove Node[index] of instance
        '''
        self.isValid(index)
        i = 0
        pre = self.head
        if index == 0:
            self.head = pre.next
        else:
            while i < index - 1:
                pre = pre.next
                i += 1
            aft = pre.next.next
            pre.next = aft
        self.length -= 1

    def __repr__(self):
        values = []
        i = self.head
        while i != None:
            values.append(i.value)
            i = i.next
        return f'{values}'
            
if __name__ == '__main__':
    l1 = LinkedList()
    l1.append(20)
    l1.append(30)
    l1.append(5)
    l1.insert(0, 3)
    l1.remove(0)
    print(l1)
