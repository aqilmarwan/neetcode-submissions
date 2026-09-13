# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
            if not p and not q:
                return True
                # needs to check
                    # i) if p and q is the same lenght
                    # ii) if p and q is children(right and left) node's val is identical
            if p and q and p.val == q.val:
                return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left) 
            else:
                return False