# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None or head.next.next is None:
            return head 
        head2 = head.next
        prev = head
        temp = head2
        while prev.next!=None and temp.next!=None:
            prev.next = temp.next
            temp.next = temp.next.next 
            prev = prev.next
            temp = temp.next
        prev.next = head2
        return head
        
        