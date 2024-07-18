# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Helper function to check balance and compute height
        def helper(root: Optional[TreeNode]) -> int:
            # Basecase is a Null Node, return 0
            if not root:
                return 0
            
            # Collect information regarding balance of node
            leftHeight = helper(root.left)
            rightHeight = helper(root.right)
            if abs(rightHeight - leftHeight) > 1:
                nonlocal balanced
                balanced = False
                return 0
            
            # Recursively return the max between height of left node and right node and add one for current node.
            return max(leftHeight, rightHeight) + 1

        # Create variable to hold balance information
        balanced = True

        # Call the function to check balance of each node
        helper(root)

        # Return the balance
        return balanced