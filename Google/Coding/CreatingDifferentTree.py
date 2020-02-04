""" Creating Types of tree"""
Count = [10]
class Tree:
    def __init__(self, x):
        self.right = None
        self.left = None
        self.val = x

    ''' 
    Binary Tree:
            Accept number
    '''
    def insert(self, a):
        if self.val:
            if self.val > a:
                if self.left is None:
                    self.left = Tree(a)
                else:
                    self.left.insert(a)
            elif self.right is None:
                self.right = Tree(a)
            else:
                self.right.insert(a)
    '''
    Binary Tree:
        Accept List
    '''
    def insertList(self, l):
        for i in l:
            if self.val:
                if self.val > i:
                    if self.left is None:
                        self.left = Tree(i)
                    else:
                        self.left.insert(i)
                elif self.val < i:
                    self.right = Tree(i)
                else:
                    self.right.insert(i)



    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.val)
        if self.right:
            self.right.printTree()


def print2DUtils(root,space):
    if root is None:
        return
    space += Count[0]

    print2DUtils(root.right, space)
    for i in range(Count[0], space):
        print(end = " ")
    print(root.val)
    print2DUtils(root.left, space)



def print2D(root):
    print2DUtils(root, 0)

if __name__ == "__main__":
    root = Tree('A')
    root.insert('a')
    root.insert('a')
    root.insert('a')
    root.insert('b')
    print2D(root)