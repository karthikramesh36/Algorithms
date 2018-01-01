class stack:
    def __init__(self):
        self.items = []

    def size(self):
        return int(len(self.items))

    def isEmpty(self):
        return self.items==[]

    def pop(self):
        return self.items.pop()

    def push(self,value):
        self.items.append(value)

    def peek(self):
        return self.items[len(self.items)-1]
