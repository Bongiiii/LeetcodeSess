# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, s):
            # Collect the values and build string
            if s != "":
                s += "->"
            s += str(node.val)

            # At a leaf node add built string to results
            if not node.left and not node.right: 
                res.append(s)

            # Progress to left node and right node
            if node.left: 
                dfs(node.left, s)
            if node.right: 
                dfs(node.right, s)

        # Create results array
        res = []

        # Call helper function to build results
        dfs(root, "") 

        # Return results
        return res