"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: head is the head of the linked list
    @return: head of linked list
    """
    def deleteDuplicates(self, head):
        # write your code here
        if head is None:
            return head
        node = head
        while node.next is not None:
            print(node.val)
            while node.next.val == node.val:
                node.next = node.next.next
                if node.next is None:
                    return head
            node = node.next
        return head

    def deleteDuplicates2(self, head):
        if head is None:
            return head
        
        node = head
        previous = ListNode(None, next=head)
        while node.next is not None:
            flag = 0
            while node.val == node.next.val:
                flag = 1
                node.next = node.next.next
                if node.next is None:
                    previous.next = node.next
                    return head
            if flag == 1:
                previous.next = node.next
            else:
                previous = previous.next             
            node = node.next
            
        return head

if __name__ == "__main__":
    l1 = [1,2,2,3,4]