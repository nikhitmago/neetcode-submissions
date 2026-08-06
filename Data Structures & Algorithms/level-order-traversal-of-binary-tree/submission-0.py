# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        output = [[1],[2,3],[4,5,6,7]]
        '''

        def dfs(root, height):
            if not root:
                return
            
            if len(output) == height:
                output.append([root.val])
            else:
                output[height].append(root.val)
            
            dfs(root.left, height+1)
            dfs(root.right, height+1)
        
        output = []
        dfs(root, 0)
        return output