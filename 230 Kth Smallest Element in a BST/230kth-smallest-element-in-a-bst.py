# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Create a helper function that processes in-order traversal while reducing k to help identify kth node
            def helper(root: TreeNode):
                nonlocal kthNode 
                nonlocal k

                # Base Case: Check if the tree is empty or k is less than 0. If it is, return. We have completed search.
                if not root or k < 0:
                    return

                # Call helper on left child
                helper(root.left)

                # Reduce k and check if k is 0, if so set kth node and return
                k -= 1
                if k == 0:
                    kthNode = root.val
                    return

                # Call helper on right child
                helper(root.right)

            # Create variable to hold kthNode
            kthNode = 0

            # Call helper function on root
            helper(root)

            # Return kthNode
            return kthNode

