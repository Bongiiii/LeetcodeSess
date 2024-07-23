# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []

        if not root:
            return levels

        def bfs(node, current_level):
            if not node:
                return

            if len(levels) == current_level:
                levels.append([])

            levels[current_level].append(node.val)

            if node.left:
                bfs(node.left, current_level + 1)

            if node.right:
                bfs(node.right, current_level + 1)

        bfs(root, 0)
        return levels