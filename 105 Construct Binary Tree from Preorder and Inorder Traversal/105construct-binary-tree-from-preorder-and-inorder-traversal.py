from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Basecase, if inorder array does not exist.
        if not inorder:
            return None
        
        # Take the first item from preorder to reflect pre-order traversal
        rootVal = preorder.pop(0)
        root = TreeNode(rootVal)

        # Find index of root node within in-order traversal to split between left child and right child
        index = inorder.index(rootVal)

        # Recursively build left and right child
        root.left = self.buildTree(preorder, inorder[:index])
        root.right = self.buildTree(preorder, inorder[index+1:])

        # Return root
        return root
