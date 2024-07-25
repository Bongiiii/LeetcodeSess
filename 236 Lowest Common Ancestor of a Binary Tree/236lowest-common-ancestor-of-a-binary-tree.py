# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Basecase: When we find p, q, or reach None, return the root. This lets the parent know p, q, or None children is available to it.
        if not root or p == root or q == root:
            return root

        # Recursively check left side and right side
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right,p, q)

        # If both left and right is available, then we have found it. Return the current root.
        if left and right:
            return root
        
        # Otherwise let parent know that what we have currently, because the LCA is higher up the tree
        return left if left else right