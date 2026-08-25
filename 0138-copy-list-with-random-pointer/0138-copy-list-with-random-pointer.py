"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        dicti = {None:None}
        curr = head
        while curr:
            new_Node = Node(curr.val)
            dicti[curr] = new_Node
            curr = curr.next
        curr = head 
        while curr:
            dicti[curr].next = dicti[curr.next]
            dicti[curr].random = dicti[curr.random]
            curr = curr.next 
        return  dicti[head]

        