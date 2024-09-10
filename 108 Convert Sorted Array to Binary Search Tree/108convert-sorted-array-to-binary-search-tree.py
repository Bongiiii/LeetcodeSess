# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Understand:
        input: ascending order sorted array with integers, output: height-balanced binary search tree

        Match:
        BST
        recursion

        Plan:
        BST - left < root < right
        so I will take advantage of that 
        implement a helper function that builds a tree

        R/E:
        s/c = t/c = O(N)
        """
        def build_tree(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            
            root.left = build_tree(left, mid - 1)
            root.right = build_tree(mid + 1, right)
            
            return root
        
        return build_tree(0, len(nums) - 1)