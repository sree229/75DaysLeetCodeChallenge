# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        slow = head
        fast = head
        while fast is not None :
            slow = slow.next
            fast = fast.next.next
        prev = None
        curr = slow
        while  curr!=None:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
        ptr1 = head
        ptr2 = prev
        maxsum = 0
        while ptr2!=None :
            if  maxsum < ptr1.val+ptr2.val :
                maxsum = ptr1.val+ptr2.val
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return maxsum