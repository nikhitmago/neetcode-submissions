# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        '''
        preorder = [3,9,20,15,7]
        inorder = [9,3,15,20,7]
        '''

        def dfs(left, right):
            if left > right:
                return None

            # Create node using preorder index and increment
            val = preorder[self.preorder_idx]
            root = TreeNode(val)
            self.preorder_idx += 1

            # Find inorder index and recurse L and R pointers
            inorder_idx = inorder_indices[val]
            root.left = dfs(left, inorder_idx-1)
            root.right = dfs(inorder_idx+1, right)

            return root


        self.preorder_idx = 0
        inorder_indices = {val: i for i, val in enumerate(inorder)}
        return dfs(0, len(inorder)-1)