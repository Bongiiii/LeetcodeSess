# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def heightFinder(node):
            if not node:
                return 0

            leftt, rightt = heightFinder(node.left), heightFinder(node.right)

            if (leftt == -1) or (rightt == -1) or abs(leftt - rightt) > 1:
                return -1

            return 1 + max(leftt,rightt)

        return heightFinder(root) >= 0
            