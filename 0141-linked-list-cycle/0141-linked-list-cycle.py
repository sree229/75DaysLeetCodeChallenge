# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # l1= []
        # ptr = head
        # while ptr!=None :
        #     if ptr in l1 :
        #         return True
        #     l1.append(ptr)
        #     ptr = ptr.next
        # return False
        slow = head
        fast = head
        while (fast!=None and fast.next!=None) :
            slow = slow.next
            fast = fast.next.next
            if slow==fast :
                return True
        return False
