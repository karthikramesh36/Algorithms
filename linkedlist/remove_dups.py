from linkedlistnode import linkedlist
def find_dups(ll):
    if ll.head is None:
        return None

    curr=ll.head
    seen=set([curr.value])
    while curr.next != None:
        if curr.next.value in seen:
            curr.next=curr.next.next
        else:
            seen.add(curr.next.value)
            curr=curr.next
    return ll

L=linkedlist()
L.add(5)
L.add(6)
L.add(7)
L.add(5)
L.add(8)
print(find_dups(L))
