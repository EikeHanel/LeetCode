# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
# #         self.right = right
# class Solution:
#     def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
#         class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def checkPath(self, tree_node, list_node):
        # Base case: if we reach the end of the linked list, we return True.
        if list_node is None:
            return True
        # If the tree node is None or values don't match, return False.
        if tree_node is None or tree_node.val != list_node.val:
            return False
        # Recursively check both left and right subtrees to see if the next list node matches.
        return (self.checkPath(tree_node.left, list_node.next) or 
                self.checkPath(tree_node.right, list_node.next))

    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """
        # If the tree is empty, return False (no path can be found)
        if root is None:
            return False
        # Check if the current root of the tree matches the list
        if self.checkPath(root, head):
            return True
        # Recursively check the left and right subtrees for the match
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)