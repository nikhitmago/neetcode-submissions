# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    count = 0
    res = None
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        k = 4
        root = 4
        
        count = 1
        res = 4
        
        '''        
        
        def dfs(root):
            if not root:
                return

            dfs(root.left)
            
            self.count += 1
            if self.count == k:
                self.res = root.val
            
            dfs(root.right)
        
        self.res = root.val
        dfs(root)
        return self.res