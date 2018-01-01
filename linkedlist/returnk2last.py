from linkedlistnode import linkedlist

def return_kth_to_last(ll,k):
    p1= ll.head
    p2= ll.head
    #we dont know the length of ll
    for i in range(k):
        if p1 is None:
            return None
        p1=p1.next
    while p1.next != None:
        p1=p1.next
        p2=p2.next

    return p2     
