# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        ans = []
        def bfs(root,level):
            if not root :
                return 
            if len(ans) == level :
                ans.append([])
            ans[level].append(root.val)
            bfs(root.left,level+1)
            bfs(root.right,level+1)
        bfs(root,0)
        return ans


        




        