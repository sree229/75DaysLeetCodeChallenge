# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None :
            return head
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        ptr1 = dummy1
        ptr2 = dummy2
        curr = head 
        while curr!=None :
            if curr.val <  x:
                ptr1.next = curr
                ptr1 = ptr1.next
            else :
                ptr2.next = curr
                ptr2 = ptr2.next
            curr = curr.next 
        ptr2.next = None
        ptr1.next = dummy2.next
        return dummy1.next 
             