# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        Understand:
        input - two arrays, output - bst
        prob summary - given two arrays, construct a bst. 

        Match:
        bst
        two pointer
        recursion

        Plan:
        inorder traversal is left, root, right, postorder is left, right, root
        also all elements before the root in inorder traversal are left nodes and the other after are right nodes
        take last element in postorder as we know its always tje root
        then append left as the first element in inorder 
        so we know for left we consider inorder, and right we consider postorder but from the back

        R/E:
        s/c = O(N), recursive calls
        t/c = O(N^2), caters for the index lookups

        """
         # Base case: if inorder or postorder is empty, return None
        if not inorder or not postorder:
            return None

        # Step 1: The root is the last element of the postorder traversal
        root_val = postorder.pop()
        root = TreeNode(root_val)
        
        # Step 2: Find the index of the root in the inorder traversal
        inorder_index = inorder.index(root_val)
        
        # Step 3: Recursively build the right subtree first and then the left subtree
        # We do right first because postorder processes root -> right -> left
        root.right = self.buildTree(inorder[inorder_index + 1:], postorder)
        root.left = self.buildTree(inorder[:inorder_index], postorder)
        
        return root