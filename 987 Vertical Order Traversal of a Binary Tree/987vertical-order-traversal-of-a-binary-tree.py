# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque,defaultdict
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        # Dictionary to store nodes based on their column positions
        column_nodes = defaultdict(list)
        
        # Queue for level order traversal
        queue = deque([(root, 0, 0)])  # (node, column, row)

        # Perform level order traversal
        while queue:
            level_size = len(queue)
            level_nodes = []

            for _ in range(level_size):
                node, col, row = queue.popleft()
                column_nodes[col].append((row, node.val))  # Store node along with its row number

                if node.left:
                    queue.append((node.left, col - 1, row + 1))
                if node.right:
                    queue.append((node.right, col + 1, row + 1))
        
        # Sort nodes at each column position based on their row numbers and values
        result = []
        for col in sorted(column_nodes.keys()):
            sorted_nodes = sorted(column_nodes[col])
            result.append([node[1] for node in sorted_nodes])
        
        return result
