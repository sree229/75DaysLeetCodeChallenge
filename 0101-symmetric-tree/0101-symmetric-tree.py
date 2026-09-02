# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def first_part(root):
            if not root or (not root.left and not root.right):
                return root
            elif not root.left :
                root.left = root.right
                root.right = None 
            elif not root.right :
                root.right = root.left
                root.left = None 
            else :
                temp = root.left
                root.left = root.right
                root.right = temp
            first_part(root.left)
            first_part(root.right)
        first_part(root.left)
        l = []
        def traversal(root):
            if not root :
                l.append(None)
                return root
            l.append(root.val)
            traversal(root.left)
            traversal(root.right)
            return l
        l1 = traversal(root.left)
        l = []
        l2 = traversal(root.right)
        if l1 == l2 :
            return True
        return False