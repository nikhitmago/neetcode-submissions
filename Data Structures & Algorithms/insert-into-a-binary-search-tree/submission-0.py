# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        '''
        cur = None
        prev = 9
        '''
        cur, prev = root, None
        while cur:
            prev = cur
            if val > cur.val:
                cur = cur.right
            else:
                cur = cur.left
        
        new_node = TreeNode(val=val)
        if prev == None:
            return new_node
        else:
            if val > prev.val:
                prev.right = new_node
            else:
                prev.left = new_node
        
        return root