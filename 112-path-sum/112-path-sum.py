# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        Sum=0
        if root is None:
            return False
        Sum+=root.val
        if targetSum==Sum and root.left is None and root.right is None:
            return True 
        return self.hasPathSum(root.left,targetSum-Sum) or self.hasPathSum(root.right,targetSum-Sum)
        
        