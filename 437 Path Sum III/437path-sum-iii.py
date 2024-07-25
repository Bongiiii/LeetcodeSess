# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
          # Create a helper function to process each node and flag for root node to prevent repeated calls to helper from same node. 
        def helper(root: Optional[TreeNode], targetSum: int, isRoot: bool):
            nonlocal numberOfPaths

            # Set basecase to root is None, return
            if not root:
                return 

            # Upon reaching a targetSum of zero, increase number of paths by 1
            if targetSum - root.val == 0:
                numberOfPaths += 1
            
            # Recursively progress through entire tree from previous node
            helper(root.left, targetSum - root.val, False)
            helper(root.right, targetSum - root.val, False)

            # Recursive progress through entire tree from current node
            if isRoot:
                helper(root.left, targetSum, True)
                helper(root.right, targetSum, True)

        # Create variable to hold number of paths found
        numberOfPaths = 0

        # Call helper function to populate number of paths found
        helper(root, targetSum, True) 

        # Return the number of paths found
        return numberOfPaths