def reverse(llist):
    prev = None
    curr = llist
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    llist = prev
    return llist