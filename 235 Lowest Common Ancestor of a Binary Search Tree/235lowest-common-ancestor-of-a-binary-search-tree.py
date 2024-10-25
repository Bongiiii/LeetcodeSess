# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        since it is a binary search tree, take advantage of the sorted small to the left and the right greater than root
        so if p and q are both smaller than the root, then traverse the left side of the tree
        elif greater than the root, traverse the right side of the tree
        else return the root/ traverse both sides
        """
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        else:
            return root