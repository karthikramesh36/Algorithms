class node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

    def getdata(self):
        return self.value

    def getleftchild(self):
        return self.left

    def getrightchild(self):
        return self.right

class tree:
    def __init__(self,root):
        self.root=root
