# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        -this tree is not a tree that follows left<root<right
        dfs is my best shot, add nodes as i traverse, subtract a node when i backtrack
        """
        def dfs(node, sumSofar):
            #base case, no tree
            if not node:
                return False

            #else, add the node val to sum
            sumSofar += node.val

            #if you have found a leaf, check if sum matches target
            if not node.left and not node.right:
                return sumSofar == targetSum

            #else, you still have nodes to reach
            return dfs(node.left, sumSofar) or dfs(node.right, sumSofar)


        return dfs(root,0)
            