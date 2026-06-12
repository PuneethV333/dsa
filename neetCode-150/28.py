# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
def reverseList(head: [ListNode]) -> [ListNode]:  # noqa: F821
    prev = None
    crr = head

    while crr:
        nxt = crr.next
        crr.next = prev
        prev = crr
        crr = nxt
    return prev
