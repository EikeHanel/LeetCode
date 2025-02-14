# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root

        while cur:
            # cur = 7, q = 10, p = 12
            if cur.val < q.val and cur.val < p.val:
                cur = cur.right
            elif cur.val > q.val and cur.val > p.val:
                cur = cur.left
            else:
                return cur
        
        