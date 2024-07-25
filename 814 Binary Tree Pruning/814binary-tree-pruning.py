# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def pruneHelper(node: Optional[TreeNode]):
            # assume that leftSubTree does not contain 1
            leftSubTreeContains1 = False

            # if there is a left child, then the left subtree could have a 1, so recursively check this
            if node.left:
                leftSubTreeContains1 = pruneHelper(node.left)
            
            # assume that rightSubTree does not contain 1
            rightSubTreeContains1 = False

            # if there is a right child, then the right subtree could have a 1, so recursively check this
            if node.right:
                rightSubTreeContains1 = pruneHelper(node.right)

            # if the leftSubTree does not have a 1, it should be removed, as per the algorithm specification
            if not leftSubTreeContains1:
                node.left = None

            # if the rightSubTree does not have a 1, it should be removed, as per the algorithm specification
            if not rightSubTreeContains1:
                node.right = None

            # the subtree rooted at this node contains a 1 if:
                # 1) the root of the subtree (the current node) has value 1
                # 2) the leftSubTree contains a 1
                # 3) the rightSubTree contains a 1
            # The parent node will use this return value to determine if its child should be pruned or not
            return node.val == 1 or leftSubTreeContains1 or rightSubTreeContains1
        
        # calling pruneHelper on the root tells us if the tree has a 1 or not
        treeHas1 = pruneHelper(root)

        # if the tree does not contain a 1, then all nodes (including the root) should be removed
        if not treeHas1:
            return None
        
        # otherwise, return the pruned tree
        return root