# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        def finding(root,subRoot):
            if not root and not subRoot :
                return True
            elif root and subRoot :
                if root.val != subRoot.val :
                    return False
            else :
                return False
            return finding(root.left,subRoot.left) and finding(root.right,subRoot.right)
        def firstNode(root,subRoot) :
            if not root:
                return False
            return finding(root,subRoot) or firstNode(root.left,subRoot) or firstNode(root.right,subRoot)
        return firstNode(root,subRoot)
    
        
          