# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        def dfs(root, height):
            if not root:
                return
            
            if len(output) == height:
                output.append([])
            
            output[height].append(root.val)
            dfs(root.right, height+1)
            dfs(root.left, height+1)
        
        output = []
        dfs(root, 0)
        flattened_output = [l[0] for l in output]
        return flattened_output