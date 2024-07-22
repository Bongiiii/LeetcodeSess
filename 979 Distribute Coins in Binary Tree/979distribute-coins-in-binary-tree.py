# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
        
        def dfs(node):
            if not node:
                return 0
            
            left_balance = dfs(node.left)
            right_balance = dfs(node.right)
            
            # Current node's balance: number of coins - 1 (as each node needs 1 coin)
            current_balance = node.val + left_balance + right_balance - 1
            
            # The total number of moves needed is the sum of the absolute balances of the left and right subtrees
            self.moves += abs(left_balance) + abs(right_balance)
            
            return current_balance
        
        dfs(root)
        return self.moves
