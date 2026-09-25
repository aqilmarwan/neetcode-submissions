# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # DFS initally gets 0(n2), when checking left and right boudaries in every tree and subtree (-int, int) we get 0(n) linear
        # BFS approach without DFS's stack  
        def valid(node, left, right):
            if not node:
                return True

            if not (left < node.val < right):
                return False
            
            return(valid(node.left, left, node.val) and
                    valid(node.right, node.val, right))
            
        return valid(root, float("-inf"), float("inf"))

        
            




        