# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object): 
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None :
            return head
        if left == right :
            return head
        curr = head
        pos = 1
        while curr!=None :
            if pos == left :
                first = curr
            if pos == right :
                last = curr
                break
            curr = curr.next 
            pos+=1
        start = head
        while start!=first and start.next!=first :
            start = start.next
        curr = first
        prev = last.next
        while prev!=last :
            after = curr.next
            curr.next = prev
            prev= curr
            curr = after
        if head == first :
            return prev
        start.next = prev
        return head
        