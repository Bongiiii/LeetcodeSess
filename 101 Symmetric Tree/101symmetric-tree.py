# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Understand:
        input: binary tree, output: boolean
        problem summary: given a binary tree, determine if it is a mirror of itsekf or not.

        Clarifying qns and comments:
        empty is not possible as the least is a tree with one node/ a leaf

        Match:
        binary tree
        dfs/ recursion

        Plan:
        handle the base case first, if leaf, return true
        implement a helper function that validates mirrors to be used for recursively
        recursively call on the left and right chn AND compare values
        if they differ, early return false
        else continue till you reach the leaf chn of the tree

        R/E:
        s/c = O(N), recursive calls
        t/c = O(N), n being the number of nodes on the tree as all nodes are visited

        """
        #base case, just a leaf
        def validMirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if not left and not right:
                return True
            
            #contains one child 
            if not left or not right:
                return False

            #else part
            return (left.val == right.val 
            and validMirror(left.right, right.left) 
            and validMirror(left.left, right.right))

            
        return validMirror(root, root)