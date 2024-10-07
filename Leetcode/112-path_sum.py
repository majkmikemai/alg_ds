from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:  # Base case if there is a node
            return False

        targetSum -= root.val
        # Sort of as appending the value to an array
        # Recursively remove until reaching leaf node and quit recursion if
        # targetSum = 0

        # Base case if the sum of nodes = targetsum
        if root.left is None and root.right is None:
            return targetSum == 0

        if self.hasPathSum(root.left, targetSum):
            return True
        if self.hasPathSum(root.right, targetSum):
            return True

        targetSum += root.val

        return False
