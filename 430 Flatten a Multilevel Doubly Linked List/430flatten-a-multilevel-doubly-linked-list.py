"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        U:
        input - multi level doubly linked list, output - singly doubly linked list

        --- attach child nodes then the nodes after the child, so preorder traversal vibes

        M:
        dfs
        backtracking
        graph / preorder traversal

        P:
        create a temporal empty node to use for creating the flattened doubly linked list.
        when traversing store the next node after child in a placeholder so as to be able to add after 
         fulfilling all child nodes
        
        I:
        R:
        s/c = O(d), d - depth of the list before flattening; t/c = O(n), n - number of nodes
        E:
        """
        def dfs(prevNode, currNode):
            #base case, no nodes to flatten
            if not currNode:
                return prevNode

            #connecting the prev and curr to create the doubly linked list
            prevNode.next = currNode
            currNode.prev = prevNode

            #storing our next after child
            placeholder = currNode.next

            #recursively exploring child nodes
            tail = dfs(currNode, currNode.child)

            #flatten that child after recursively exploring it
            currNode.child = None

            #this ensures backtracking and adding of all placeholders
            return dfs(tail, placeholder)

        if not head:
            return None

        #final list to be returned
        temp = Node(0, None, head, None)

        #treat the temp as prev and head as next
        dfs(temp, head)

        #remove pointer from temp
        temp.next.prev = None

        return temp.next