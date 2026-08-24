# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        ptr = dummy
        carry = 0
        while l1 != None and l2!=None :
            res = carry + l1.val + l2.val
            if res > 9 :
                carry = 1
                digit = res%10
            else :
                carry = 0
                digit = res
            new_LL = ListNode(digit)
            ptr.next = new_LL
            ptr = ptr.next
            l1 = l1.next
            l2 = l2.next 
        while l1 is not None :
            res = carry+ l1.val
            if res > 9 :
                carry = 1
                digit = res%10
            else :
                carry = 0
                digit = res
            new_LL = ListNode(digit)
            ptr.next = new_LL
            ptr = ptr.next
            l1 = l1.next
        while l2 is not None : 
            res = carry+ l2.val
            if res > 9 :
                carry = 1
                digit = res%10
            else :
                carry = 0
                digit = res
            new_LL = ListNode(digit)
            ptr.next = new_LL
            ptr = ptr.next
            l2 = l2.next
        if carry == 1 :
            new_LL = ListNode(1)
            ptr.next = new_LL
        return dummy.next