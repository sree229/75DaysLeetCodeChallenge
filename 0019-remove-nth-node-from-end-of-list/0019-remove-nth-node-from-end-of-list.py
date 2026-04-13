# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        count = 0
        while temp!=None :
            count+=1
            temp = temp.next 
        val = count-n
        if val==0:
            head = head.next
            return head
        i = 0
        temp = head
        while temp!=None and i<val:
            prev = temp
            temp = temp.next
            i+=1
        if temp!=None:
            prev.next = temp.next
            return head
        
        