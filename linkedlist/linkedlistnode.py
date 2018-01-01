class llnode:
    def __init__(self,value=None):
        self.value= value
        self.next= None
    def getdata(self):
        return self.value
    def getnext(self):
        return self.next
    def __str__(self):
        return str(self.value)
    def setnext(self,newvalue):
        self.next = newvalue

class linkedlist:

    def __init__(self,head=None):
        self.head=head
    def __iter__(self):
        current =self.head
        while current:
            yield current
            current=current.next

    def add(self,value):
        newnode=llnode(value)
        newnode.setnext(self.head)
        self.head=newnode
    def size(self):
        curr=self.head
        count=0
        while(curr):
            count+=1
            self=self.getnext()
        return count

    def search(self,value):
        curr=self.head
        found =False
        while(curr):
            if (curr.getdata() == value):
                found =True
            else:
                curr=curr.getnext()
        if curr == None:
            raise ValueError("data not in list")
        return current

    def delete(self,value):
        curr=self.head
        found =False
        prev=None
        while(curr and found is False):
            if (curr.getdata() == value):
                found =True
            else:
                prev=curr
                curr=curr.getnext()
        if curr == None:
            raise ValueError("data not in list")
        if prev == None:
            self.head =None
        else:
            prev.setnext(curr.getnext())
        return curr

    def __str__(self):
            curr=self.head
            l=[]
            while(curr):
                l.append(str(curr.value))
                curr=curr.getnext()
            return '->'.join(l)

    def reverse(self):
        curr=self.head
        prev=None
        nextnode=None
        while(curr):
            nextnode=curr.getnext()

            curr.setnext(prev)

            prev=curr
            curr=nextnode
        self.head=prev

L=linkedlist()
L.add(5)
L.add(6)
L.add(7)
L.add(8)
L.reverse()
print(L)
