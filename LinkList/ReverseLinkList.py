class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        # write your code here
        if head is None:
            return head
        node = head 
        temp = head
        previous = None
        while node.next is not None:
            temp = node.next
            node.next = previous
            previous = node
            node = temp
        node.next = previous
        return node

    """
    @param head: ListNode head is the head of the linked list 
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """
    def reverseBetween(self, head, m, n):
        # write your code here
        if head is None:
            return head
        node = head
        previous = None
        idx = 1
        while idx < m:
            previous = node
            node = node.next
            idx += 1
        
        start = previous
        startreverse = node
        
        if node.next is not None:
            previous = node
            node = node.next
            idx += 1
        
        while idx < n and node.next is not None:
            temp = node.next
            node.next = previous
            previous = node
            node = temp 
            idx += 1
            
        end = node.next
        node.next = previous 
        
        if start is not None:
            start.next = node
        else:
            head = node
        startreverse.next = end
        
        return head