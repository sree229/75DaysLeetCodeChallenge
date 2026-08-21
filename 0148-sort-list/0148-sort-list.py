# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        if head == None or head.next == None :
            return head 
        slow = head
        fast = head 
        while fast != None and fast.next != None :
            ptr = slow 
            slow = slow.next 
            fast = fast.next.next 
        ptr.next = None 
        left = head 
        right = slow
        left = self.sortList(left)
        right = self.sortList(right) 
        p1 = left 
        p2 = right 
        dummy = ListNode(0)
        curr = dummy 
        while p1 != None and p2 != None :
            if p1.val <= p2.val :
                curr.next = p1
                p1 = p1.next 
            else :
                curr.next = p2
                p2 = p2.next 
            curr = curr.next
        if p1!=None :
            curr.next = p1
        if p2!=None :
             curr.next = p2 
        return dummy.next 