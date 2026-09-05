# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        maxi = [0]
        def diameter(root):
            if not root :
                return 0
            lh = diameter(root.left)
            rh = diameter(root.right)
            maxi[0]  = max(maxi[0],lh+rh)
            return 1+max(lh,rh)
        diameter(root)
        return maxi[0]
        
   
      


            

        