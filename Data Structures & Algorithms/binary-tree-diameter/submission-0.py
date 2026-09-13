# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # Diameter is max.right + max.left form root(+1)
        # Height of both right and left
        # approach, needs global var to update diameter from height (right, left)

        self.res = 0

        def dfs(cur):
            if not cur:
                return 0

            maxR = dfs(cur.right)
            maxL = dfs(cur.left)

            self.res = max(self.res, maxR + maxL)
            return 1 + max(maxR, maxL)
        dfs(root)
        return self.res




