# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Understand:
        - Input: binary tree root node, output: list of values in inorder traversal.
        - Edge case(s): empty tree (return empty list).

        Match:
        - Recursion, Inorder traversal (left -> root -> right), DFS, Binary trees.

        Plan:
        - Inorder traversal order: left, root, right.
        - Initialize an empty array to store the result.
        - Base case: if the tree is empty, return the empty array.
        - Use a helper function to traverse:
          * Recursively call the left subtree.
          * Append the current node's value.
          * Recursively call the right subtree.
        - Return the result array.

        R/E:
        - Time complexity: O(N), where N is the number of nodes (all nodes are visited).
        - Space complexity: O(N), for the recursion stack in the worst case (skewed tree).
        """
        output = []

        def inorder(node):
            #base case
            if not node:
                return []

            #recursively traverse left nodes
            inorder(node.left)

            #append the node
            output.append(node.val)

            #check right side, then first check if you have seen the left most node
            inorder(node.right)
            
        #recursively call helper on whole root
        inorder(root)

        return output