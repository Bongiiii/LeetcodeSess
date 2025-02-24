# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
         # Initialize the level to 0 (0-indexed, so even)
        level = 0
      
        # Initialize the queue with the root node
        queue = deque([root])
      
        # Traverse the tree by levels
        while queue:
            # Depending on the current level, set the previous value accordingly
            # For even levels, we start comparing from the smallest possible value (0)
            # For odd levels, we start comparing from the largest possible value (infinity)
            previous_value = 0 if level % 2 == 0 else float('inf')
          
            # Process all nodes in the current level
            for _ in range(len(queue)):
                node = queue.popleft()

                # Check the Even-Odd Tree condition for the current node
                # At even levels, values must be odd and strictly increasing
                if level % 2 == 0 and (node.val % 2 == 0 or previous_value >= node.val):
                    return False
                # At odd levels, values must be even and strictly decreasing
                if level % 2 == 1 and (node.val % 2 == 1 or previous_value <= node.val):
                    return False
              
                # Update the previous value for the next comparison
                previous_value = node.val
              
                # Add child nodes to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
          
            # Move to the next level
            level += 1
            
        # If all conditions are met, return True
        return True