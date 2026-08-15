# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None or k==0:
            return head
        curr = head
        n = 0
        while curr!=None :
            n+=1
            curr= curr.next
        k = k%n
        if k ==0 :
            return head
        pos = n-k
        curr = head
        index = 0
        prev = None
        while curr!=None and index!=pos:
            prev = curr
            curr = curr.next
            index+=1 
        prev.next = None 
        ptr = curr
        while curr.next!=None :
            curr = curr.next
        curr.next = head
        head = ptr
        return head


        
        
        

      
    

                    