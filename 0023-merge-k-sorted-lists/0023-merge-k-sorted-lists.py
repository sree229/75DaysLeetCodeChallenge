# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if lists == []  :
            return   
        res = lists[0] 
        i = 1
        while i <len(lists) :
            curr2 = lists[i]
            curr1 = res 
            res = ListNode(0)
            curr3 = res
            while curr1 is not None and curr2 is not None :
                if curr1.val <= curr2.val :
                    curr3.next = curr1 
                    curr1 = curr1.next 
                else :
                    curr3.next = curr2 
                    curr2 = curr2.next
                curr3 = curr3.next 
            if curr1 is not None :
                curr3.next =  curr1 
            if curr2 is not None :
                curr3.next = curr2
            res = res.next 
            i+=1
        return res


        