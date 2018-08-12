"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        length = len(lists)
        if length == 0:
            return None
        if length == 1:
            return lists[0]
            
        mid = int(length/2)
        leftnode = self.mergeKLists(lists[:mid])
        rightnode = self.mergeKLists(lists[mid:])
        
        return self.merge2Lists(leftnode, rightnode)
        
    def merge2Lists(self, left, right):
        if left is None:
            return right
        if right is None:
            return left
        
        start = ListNode(None)
        node = start
        while right is not None and left is not None:
            if right.val < left.val :
                node.next = right
                right = right.next
            else:
                node.next = left
                left = left.next
            node = node.next
        if right is None:
            node.next = left
        if left is None:
            node.next = right
            
        return start.next
        

