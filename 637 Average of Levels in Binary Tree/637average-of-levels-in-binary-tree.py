# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """
        Level order traversal(bfs) = root, left, right
        """
        store = []
        #level order traversal helper func
        def levlOrdHelper(root, level):
            #base case, empty tree
            if not root:
                return

            #initialize store, sum of nodes on that level, and count of nodes on that level
            if len(store) <= level:
                store.append([0,0])

            #be keeping the sum at each level
            store[level][0]+=root.val
            store[level][1]+=1

            #add children
            levlOrdHelper(root.left, level+1)
            levlOrdHelper(root.right, level+1)

        #call helper func recursively on whole tree
        levlOrdHelper(root, 0)

        avgVal = []

        for levlSum, lvlnodeCount in store:
            avgVal.append(levlSum/lvlnodeCount)

        return avgVal