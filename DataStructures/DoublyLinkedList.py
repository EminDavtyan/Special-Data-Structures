class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 1

    def isValid(self, index):
        assert isinstance(index, int), 'Index should be int'
        assert index >= 0, 'Invalid index, negative index'
        assert index <= self.length, f'Index out of range ({self.length-1})'

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
            new_node.prev = self.tail
            self.tail = new_node
            self.length += 1

    def prepend(self, value):
        '''
        Prepend new Node(tail node)
        '''
        new_node = Node(value)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1

    def insert(self, index: int, value):
        '''
        Insert new Node[index]
        '''
        new_node = Node(value)
        if index==0:
            self.prepend(value)
            return
        if index >= self.length:
            self.append(value)
            return
        else:         
            leader = self.traversetoindex(index - 1)
            holder = leader.next
            leader.next = new_node
            new_node.next = holder
            new_node.prev = leader
            holder.prev = new_node
            self.length+=1

    def remove(self, index: int):
        '''
        Remove Node[index] of instance
        '''
        self.isValid(index)
        if index==0:
            self.head=self.head.next
            self.length-=1
            return
        if index == self.length-1:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return
        leader = self.traversetoindex(index-1)
        unwanted_node = leader.next
        holder = unwanted_node.next
        leader.next = holder
        holder.prev = leader
        self.length -= 1

    def traversetoindex(self,index):
        curr_node = self.head
        i = 0
        while i!= index:
            curr_node = curr_node.next
            i+=1
        return curr_node

    def __repr__(self):
        values = []
        i = self.head
        while i != None:
            values.append(i.value)
            i = i.next
        return f'{values}'
            
if __name__ == '__main__':
    l1 = DoublyLinkedList()
    l1.append(5)
    l1.append(10)
    l1.insert(2, 20)
    print(l1)
