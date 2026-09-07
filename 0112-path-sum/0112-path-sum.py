# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetsum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        def path(root,total_sum,targetsum) :
            if not root :
                return False 
            total_sum += root.val
            if not root.left and not root.right :
                if total_sum != targetsum :
                    return False 
                else :
                    return True
            return path(root.left,total_sum,targetsum) or path(root.right,total_sum,targetsum)
        return path(root,0,targetsum)