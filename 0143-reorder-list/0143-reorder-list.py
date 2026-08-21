# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None :
            return head
        fast = head
        slow = head
        while fast != None and fast.next!=None :
            ptr = slow 
            slow = slow.next
            fast = fast.next.next 
        ptr.next = None
        curr = slow 
        prev = None 
        while  curr!=None:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after 
        curr1 = head
        curr2 = prev
        dummy = ListNode(0)
        curr = dummy 
        while curr1!=None and curr2!=None :
            curr.next = curr1
            curr1 = curr1.next
            curr = curr.next
            curr.next = curr2
            curr2 = curr2.next
            curr = curr.next
        if curr1!=None :
            curr.next = curr1
        if curr2!=None :
            curr.next = curr2
        return dummy.next
