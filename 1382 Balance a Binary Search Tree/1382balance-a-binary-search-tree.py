# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Input - root , output - root of balanced bst
        

        Plan:
        brute force approach:
        recursively try variations of bst(left<root<right) trees 
        each node as a root in each recursion
        and check the difference between left and right nodes is <=0
        and instantly break loop and return the first balanced
         tree no need to continue

        optimal solution:
        first do an inorder traversal on the input tree
        then do a binary search dfs that finds middle node and checks if balanced, 
        this way we are likely to find faster as middle
         we always have a sort of balance

        """
        def inorderDFS(node):
            #base case empty
            if not node:
                return 
            #to get the sort effect, put nodes like left,root,right
            inorderDFS(node.left)
            ordered.append(node.val)
            inorderDFS(node.right)

        #build the tree within the bounds of the length of sorted list collect above
        def bstBuilder(i, j):
            if i > j:
                return None

            #mid = (i+j) >> 1
            mid = (i+j) // 2
            left = bstBuilder(i, mid - 1)
            right = bstBuilder(mid + 1, j)

            return TreeNode(ordered[mid],left,right)
        
        ordered = []
        inorderDFS(root)

        return bstBuilder(0, len(ordered)-1)