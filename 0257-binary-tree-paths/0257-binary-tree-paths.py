# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        
        def backtrack(root_pos, curStr):
            # Base case: if this is a leaf node, add the current path to the result
            if not root_pos.left and not root_pos.right:
                ans.append(curStr)
                return
            
            # Explore the left subtree
            if root_pos.left:
                backtrack(root_pos.left, curStr + "->" + str(root_pos.left.val))
            
            # Explore the right subtree
            if root_pos.right:
                backtrack(root_pos.right, curStr + "->" + str(root_pos.right.val))

        if root:
            backtrack(root, str(root.val))
        
        return ans