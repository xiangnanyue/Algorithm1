"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The first node of linked list
    @param x: An integer
    @return: A ListNode
    """
    def partition(self, head, x):
        # write your code here
        nodeleft = ListNode(0)
        noderight = ListNode(0)
        lefthead,righthead = nodeleft, noderight
        while head is not None:
            print(head.val)
            if head.val < x:
                nodeleft.next = head
                nodeleft = nodeleft.next
            else:
                noderight.next = head
                noderight = noderight.next
            head = head.next
        nodeleft.next = righthead.next
        noderight.next = None  # easy to forget
        return lefthead.next