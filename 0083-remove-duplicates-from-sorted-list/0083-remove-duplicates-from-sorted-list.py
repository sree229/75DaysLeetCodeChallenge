# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None :
            return head
        curr = head
        after = head.next 
        while after!= None and curr.next!=None  :
            if curr.val != after.val :
                curr.next = after 
                curr = curr.next
            after = after.next
        if not after :
            curr.next = None 
        return head 

        