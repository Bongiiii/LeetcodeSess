from collections import deque, defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []

        # Step 1: Create a map of parents
        parent_map = {}
        
        def map_parents(node, parent=None):
            if node:
                parent_map[node] = parent
                map_parents(node.left, node)
                map_parents(node.right, node)
        
        map_parents(root)
        
        # Step 2: Use BFS to find all nodes at distance k from the target
        queue = deque([(target, 0)])  # (node, current_distance)
        seen = {target}  # Set to keep track of visited nodes
        res = []
        
        while queue:
            node, current_distance = queue.popleft()
            
            if current_distance == k:
                res.append(node.val)
            
            # Check the neighbors: left child, right child, and parent
            for neighbor in (node.left, node.right, parent_map[node]):
                if neighbor and neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, current_distance + 1))
        
        return res


