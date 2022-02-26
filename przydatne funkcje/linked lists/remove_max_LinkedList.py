def remove_max(first):
    curr = first.next
    prev = first
    prev_max = prev
    curr_max = curr

    while curr is not None:
        if curr.val > curr_max.val:
            prev_max = prev
            curr_max = curr
        prev, curr = curr, curr.next

    prev_max.next = curr_max.next
    return first, curr_max.val