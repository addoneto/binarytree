class Tree:
    def __init__(self):
        self.root = None

    def addValue(self, value) :
        if self.root is None:
            self.root = Node(value)
        else :
            self.root.addValue(value)

    def search(self, value) :
        if self.root is not None :
            self.root.search(value)
        else : 
            print("Cannot search an empty tree")

    def writeArray(self, array, sorted = False):
        if sorted :
            # sort the array fist so the tree is more 'simetric'
            array.sort()

            nRootIndex = len(array) // 2 # math.floor(len(array) / 2)
            self.root = Node(array[nRootIndex])

            array.pop(nRootIndex)

        for b in array:
            self.addValue(b)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def addValue(self, value) :
        if value < self.value :
            if self.left is None:
                self.left = Node(value)
            else :
                self.left.addValue(value)

        elif value > self.value :
            if self.right is None:
                self.right = Node(value)
            else :
                self.right.addValue(value)

        # do nothing when the number is equal

    def search(self, value):
        if self.value == value:
            print(f'Found {value}')
            return
        elif value < self.value and self.left is not None:
            self.left.search(value)
        elif value > self.value and self.right is not None:
            self.right.search(value)
        else:
            print(f'Not Found {value}')

tree = Tree()
# tree.addValue(10)
# tree.addValue(3)
# tree.addValue(11)
tree.writeArray([10,3,11,50,84, 5, 7], True)

tree.search(8)
tree.search(7)