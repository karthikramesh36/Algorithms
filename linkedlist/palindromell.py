def palin(linkedlist ll):
    fast=ll.head
    faster=ll.head
    stack=[]

    while faster and faster.next:
        stack.append(fast.value)
        fast=fast.next
        faster=faster.next.next

    if faster:
        fast=fast.next

    while(fast):
        top=stack.pop()

        if top != fast.value:
            return False
        fast=fast.next

    return True
