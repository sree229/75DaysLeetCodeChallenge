# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        nums = []
        def path(root,arr,target) :
            if not root :
                return 0
            arr.append(root.val)
            if not root.left and not root.right :
                if sum(arr) == target :
                    nums.append(arr[::])
            path(root.left,arr,target) 
            path(root.right,arr,target)
            arr.pop()
        path(root,[],targetSum)
        return nums          