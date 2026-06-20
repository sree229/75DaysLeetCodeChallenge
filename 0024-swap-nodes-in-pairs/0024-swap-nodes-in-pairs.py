# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        dummy = ListNode()
        curr = head
        prev = dummy
        while curr!=None and curr.next!=None :
            after = curr.next
            curr.next = after.next
            after.next = curr
            prev.next = after
            prev = curr
            curr = curr.next
        return dummy.next