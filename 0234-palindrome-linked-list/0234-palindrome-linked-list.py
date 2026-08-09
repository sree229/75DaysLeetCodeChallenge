# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        temp = head 
        count = 0
        while temp!= None :
            count+=1
            temp = temp.next
        flag = True
        if count %2 !=0:
            flag = False
        fast = head 
        slow = head
        while fast is not None and fast.next is not None :
            slow = slow.next
            fast = fast.next.next
        if flag :
            curr = slow
        else :
            curr = slow.next
        prev = None 
        while curr!=None :
            after = curr.next 
            curr.next = prev
            prev = curr
            curr = after 
        temp1 = head
        temp2 = prev
        while temp2!=None :
            if temp1.val != temp2.val:
                return False
            temp1 = temp1.next
            temp2 = temp2.next
        return True
        
        

        
        