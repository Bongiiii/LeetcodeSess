# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Understand:
        input - binary tree root, output - array with outter right side view node values
        edge cases: empty tree, left children only tree, 

        Match:
        Binary search
        tree manipulation
        bfs
        level order traversal
        iterative approach

        Plan:
        use level order traversal, and a deque to process elements at each level
        initialize the queue with the root element
        the process runs as long as the queue is none empty
        always append the last element on each level to the resultant array

        R/E:
        s/c = O(N), n being the height of the tree
        t/c = O(M), visit all nodes
        """

        res = []
         
        #base case, empty root
        if not root:
            return res

        #none empty root
        queue = deque([root])

        while queue:
            res.append(queue[-1].val)

            for _ in range(len(queue)):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return res