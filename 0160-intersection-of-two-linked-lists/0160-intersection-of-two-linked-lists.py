# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        fast = headB 
        slow = headA
        while slow!=fast :
          slow = slow.next if slow else headB
          fast = fast.next if fast else headA
        return slow