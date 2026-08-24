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
        def reverse(ll) :
            prev = None 
            curr = ll
            while curr!= None :
                after = curr.next
                curr.next = prev
                prev = curr
                curr = after
            return prev
        head1 =  reverse(l1)
        head2 =  reverse(l2) 
        curr1 = head1
        curr2 = head2 
        carry = 0
        dummy = ListNode(0)
        ptr = dummy
        while curr1 is not None and curr2 is not None : 
            res = carry + curr1.val + curr2.val
            if res > 9 :
                carry = 1
                digit = res%10
            else :
                carry = 0
                digit = res
            new_LL = ListNode(digit)
            ptr.next = new_LL
            ptr = ptr.next
            curr1 = curr1.next
            curr2 = curr2.next
        while curr1 is not None :
            res = carry+ curr1.val
            if res > 9 :
                carry = 1
                digit = res%10
            else :
                carry = 0
                digit = res
            new_LL = ListNode(digit)
            ptr.next = new_LL
            ptr = ptr.next
            curr1 = curr1.next
        while curr2 is not None : 
            res = carry+ curr2.val
            if res > 9 :
                carry = 1
                digit = res%10
            else :
                carry = 0
                digit = res
            new_LL = ListNode(digit)
            ptr.next = new_LL
            ptr = ptr.next
            curr2 = curr2.next
        if carry == 1 :
            new_LL = ListNode(1)
            ptr.next = new_LL
        return reverse(dummy.next)

