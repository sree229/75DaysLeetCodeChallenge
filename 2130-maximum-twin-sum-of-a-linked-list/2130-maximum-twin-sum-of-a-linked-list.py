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
        curr = head
        arr = []
        while curr!=None :
            arr.append(curr.val)
            curr = curr.next
        print(arr)
        maxsum = 0
        n = len(arr)
        for i in range(len(arr)):
            if maxsum < arr[i]+arr[n-1-i] :
                maxsum = arr[i]+arr[n-1-i] 
        return maxsum