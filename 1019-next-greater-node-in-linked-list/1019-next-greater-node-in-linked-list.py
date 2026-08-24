# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        curr = head
        nums = []
        while curr!=None :
            nums.append(curr.val)
            curr = curr.next
        print(nums)
        arr = [0]*len(nums)
        stack = []
        for i in range(len(nums)) :
            while stack!=[] and nums[i] > nums[stack[-1]] :
                arr[stack[-1]] = nums[i]
                stack.pop()
            stack.append(i) 
        return arr


        