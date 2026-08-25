# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        arr = []
        curr = head 
        while curr is not None :
            arr.append(curr.val)
            curr = curr.next
        stack = []
        for i in arr:
            while  stack  and i > stack[-1] :
                stack.pop()
            stack.append(i)
        dummy = ListNode(0) 
        curr = dummy 
        for i in stack : 
            new_element = ListNode(i)
            curr.next = new_element
            curr = curr.next
        return dummy.next