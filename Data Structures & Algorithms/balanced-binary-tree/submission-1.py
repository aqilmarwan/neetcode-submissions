# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
    # Balance length right node == left node is not more than +1 difference
    # If node at root, balanced
    # Need to return 2 values [bool, height] bcs node needs to update its parent on it's height iter.

        def dfs(root):
            if not root:
                return [True, 0]
            
            right = dfs(root.right)
            left = dfs(root.left)

            # Balanced if 
                # i) right is Balance[True] = 0
                # ii) left is Balance[True] = 0
                # iii) if diff not more than 1.
                
            balanced = right[0] and left[0] and abs(right[1] - left[1]) <= 1 
            return [balanced, 1 + max(right[1], left[1])]

        return dfs(root)[0]