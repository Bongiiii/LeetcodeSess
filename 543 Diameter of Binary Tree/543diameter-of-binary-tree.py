# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0

        #dfs helper
        def dfsHelper(node):
            #base case
            if not node:
                return 0

            leftDiameter = dfsHelper(node.left)
            rightDiameter = dfsHelper(node.right)
            
            currDiameter = leftDiameter + rightDiameter

            self.maxDiameter = max(maxDiameter, currDiameter)

            return 1 + max(leftDiameter, rightDiameter)

        dfsHelper(root)

        return self.maxDiameter
