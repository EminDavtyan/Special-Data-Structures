class Node:
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return
        currentNode = self.root
        while True:
            if value < currentNode.value:
                #left
                if not currentNode.left:
                    currentNode.left = new_node
                    return
                currentNode = currentNode.left
            
            else:
                #right
                if not currentNode.right:
                    currentNode.right = new_node
                    return
                currentNode = currentNode.right

    def lookup(self, value):
        currentNode = self.root
        while currentNode:
            if  value < currentNode.value:
                #left
                currentNode = currentNode.left
            elif value > currentNode.value:
                #right
                currentNode = currentNode.right
            elif currentNode.value == value:
                return currentNode
        return False
    
    def remove(self):
        pass


    def printt(self,curr_node):
        if curr_node != None:
            self.printt(curr_node.left)
            print(str(curr_node.value))
            self.printt(curr_node.right)
    
    def print_tree(self):
        if self.root != None:
           self.printt(self.root)  
#Inorder Traversal (We get sorted order of elements in tree)


if __name__ == '__main__':
    bst1 = BinarySearchTree()
    bst1.insert(50)
    bst1.insert(20)
    bst1.insert(70)
    bst1.insert(10)
    bst1.insert(30)
    bst1.insert(60)        
    bst1.insert(80)
    bst1.print_tree()
    print(bst1.lookup(70))
