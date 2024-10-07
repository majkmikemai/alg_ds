from typing import Optional


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Basecase where there is no nodes left to search
        if not root:
            return None
        # Basecase where we have found the correct treenode
        if root.val == val:
            return root

        # check left node
        if val < root.val:
            return self.searchBST(root.left, val)

        # Check right node
        if val > root.val:
            return self.searchBST(root.right, val)
