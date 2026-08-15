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
        n =0
        while curr!=None :
            n +=1
            curr = curr.next
        k = k%n
        while k!=0 :
            temp = head
            while temp.next!=None :
                prev = temp
                temp = temp.next
            prev.next = None
            temp.next = head
            head = temp
            k-=1
        return head

                    