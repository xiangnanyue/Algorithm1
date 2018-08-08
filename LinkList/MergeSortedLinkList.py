"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
        dm = ListNode(0)
        prehead = dm
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                dm.next = l1
                l1 = l1.next
            else:
                dm.next = l2
                l2 = l2.next
            dm = dm.next
        if l1 is None:
            dm.next = l2
        else:
            dm.next = l1
        return prehead.next
            
                
            