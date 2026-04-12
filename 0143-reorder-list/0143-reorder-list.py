# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        dummy = ListNode()
        slow = head 
        fast = head
        change = slow 
        while fast!=None and fast.next!=None :
            change = slow
            slow = slow.next
            fast = fast.next.next
        change.next=None
        curr = slow
        prev = None
        while curr!=None :
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
        head1 = head
        head2 = prev
        head3 = dummy
        while head1!=None and head2!=None :
            head3.next=head1
            head1 = head1.next
            head3 = head3.next
            head3.next = head2
            head2 = head2.next
            head3 = head3.next
        if head2!=None:
            head3.next = head2
        head.next = dummy.next.next
