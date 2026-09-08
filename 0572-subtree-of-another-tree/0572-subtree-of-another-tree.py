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
        res = []
        def firstNode(root,subRoot) :
            if not root:
                return 
            if root.val == subRoot.val :
                 res.append(finding(root,subRoot))
            firstNode(root.left,subRoot)
            firstNode(root.right,subRoot)
        firstNode(root,subRoot)
        for i in res :
            if i == True :
                return True
        return False
                    
        
          