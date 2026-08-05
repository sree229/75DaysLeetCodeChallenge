# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        head1 = list1 
        head2 = list2 
        head3 = dummy 
        while head1!=None and head2!=None :
            if head1.val <= head2.val :
                head3.next = head1
                head1 = head1.next 
            else :
                head3.next = head2
                head2 = head2.next 
            head3 = head3.next
        if  head1!=None :
            head3.next = head1
        if head2!=None :
            head3.next = head2 
        return dummy.next


        