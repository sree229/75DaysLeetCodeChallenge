# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        curr = head 
        arr = []
        while curr!=None :
            arr.append(curr.val)
            curr = curr.next
        i = 0 
        d = k
        while i < len(arr) and len(arr[i:]) >= k  : 
            arr[i:d] = arr[i:d:][::-1]
            i+=k
            d+=k
        print(arr)
        curr = head 
        i = 0 
        while curr!= None :
            curr.val = arr[i]
            curr = curr.next 
            i+=1
        return head 
            


        