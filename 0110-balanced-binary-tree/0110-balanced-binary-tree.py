# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def height(root):
            if not root :
                return 0
            lh = height(root.left)
            rh = height(root.right)
            return 1+max(lh,rh)
        def balance(root):
            if not root :
                return True
            lh = height(root.left)
            rh = height(root.right)
            if abs(lh-rh) > 1 :
                return False 
            if not balance(root.left):
                return False
            if not balance(root.right):
                return False
            return True
        return balance(root)
        
        