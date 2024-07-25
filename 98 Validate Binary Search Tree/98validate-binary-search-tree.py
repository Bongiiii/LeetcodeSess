from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Create a helper function that processes tree via pre-order traversal while retaining the maximum value and minimum value of node as determined by parent nodes.
        def helper(node: Optional[TreeNode], minimumValueOfNode: int, maximumValueOfNode: int) -> bool:
            # Check if the node is None. If it is, return true. We made it to the leaf of a tree and every node along the path is valid.
            if not node:
                return True
            
            # Check if the node is within minimum and maximum range. If it is not, return false.
            if node.val <= minimumValueOfNode or node.val >= maximumValueOfNode:
                return False
            
            # Call helper on left child, when going left, update the maximum value of child node is less than parent node
            # Call helper on right child, when going right, update the minimum value of child node is greater than parent node
            return helper(node.left, minimumValueOfNode, node.val) and helper(node.right, node.val, maximumValueOfNode)

        # Call helper function on root and set minimum value of node to be negative infinite and maximum value of node to be positive infinite
        return helper(root, -math.inf, math.inf)
