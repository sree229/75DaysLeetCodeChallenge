"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head :
            return None 
        self.flatten_helper(head)
        return head
    def flatten_helper(self,curr):
        last = curr
        while curr :
            if curr.child:
                next_node = curr.next 
                tail = self.flatten_helper(curr.child)
                curr.next  = curr.child
                curr.child.prev = curr
                curr.child = None 
                tail.next = next_node
                if next_node :
                    next_node.prev = tail 
            if curr.next is None :
                last = curr
            curr = curr.next 
        return last 





