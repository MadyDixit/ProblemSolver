'''
Task 1: Check weather the Given Tree is Unival or Not.
Task 2: Count the Number of Unival Tree in the Tree.
'''

'''
Task 1:
'''
class Tree:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
    def insert(self, data):
        if self.val:
            if self.val > data:
                if self.left is None:
                    self.left = Tree(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.insert(data)
        else:
            return False

class Tasker:
    def is_unival(self,root):
        return unival_helper(root, root.val)

    def unival_helper(self, root, value):
        if root is None:
            return True
        elif root.val == value:
            return self.unival_helper(root.left, value) and self.unival_helper(root.right, value)
        return False



if __name__ == '__main__':
