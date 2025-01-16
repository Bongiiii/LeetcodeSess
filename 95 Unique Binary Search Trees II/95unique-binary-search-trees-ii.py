# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        """
        Understand:
        input - integer, output - array of arrays
            edge case - empty array(nut already handled in the constraints)

        Match:
        back tracking
        recursion
        bst

        Plan:
        bst rules: left nodes are less than the root and the right nodes are greater than the root node, and also the left right nodes are bsts
        recursively build all the structurally unique bsts with n nodes
        have an array to store the nodes of the bst nodes
        define a helper function that recursively builds bsts and takes in the start and end nodes
        left will start from the start and root node - 1, while the right node will start from root node + 1 to the end
        finally recursively call the helper function with parameters start set to 1 and end to n 

        R/E:
        s/c = t/c = O(N * C_n), C_n is the nth catalian number
        """
        #helper function
        def generate(start, end):
            
            trees = []

            #base case: if start is greater than end, there is no tree to add
            if start > end:
                trees.append(None)

            else:
                #iterate through each number in range and make it as the root
                for rootNode in range(start, end + 1):
                    #recursively generate all possible left and right nodes
                    leftTree = generate(start, rootNode - 1)

                    rightTree = generate(rootNode + 1, end)

                    # Nested loops to combine each left and right subtree with the current root node
                    for leftSubtree in leftTree:
                        for rightSubtree in rightTree:
                            # Create a new tree with the current number as the root
                            root = TreeNode(rootNode, leftSubtree, rightSubtree)
                            trees.append(root)

            return trees

        return generate(1, n)


