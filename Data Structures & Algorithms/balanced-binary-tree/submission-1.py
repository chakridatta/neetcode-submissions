# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        t = 0

        def dfs(root):       # For calculating height

            if not root:
                return 0
            
            nonlocal t

            left  = dfs(root.left)
            right = dfs(root.right) 
            
            if abs(left - right) > 1:
                t = 1

            return 1 + max(left, right)
        
        dfs(root)

        return True if t == 0 else False
