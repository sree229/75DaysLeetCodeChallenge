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
        head1 = ListNode(0)
        prev = head1
        after = curr.next
        while curr!=None and curr.next!=None :
            if curr.val!=after.val :
                prev.next = curr
                prev = prev.next
                curr = curr.next
                after = after.next 
            else :
                while after!= None and curr.val== after.val :
                    after = after.next
                prev.next = after
                curr = after
                if curr!=None :
                    after = curr.next 
        return head1.next 
