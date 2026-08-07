# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    output = 0
    
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, max_val):
            if not root:
                return
            
            if root.val >= max_val:
                self.output += 1
                max_val = root.val
            
            dfs(root.left, max_val)
            dfs(root.right, max_val)
        
        dfs(root, root.val)
        return self.output
        