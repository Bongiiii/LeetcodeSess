# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Set/Hash Map approach to detect a cycle.
        It uses extra space to store all visited nodes.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        visited_nodes = set()
        current = head

        while current is not None:
            # If the current node is already in the set, a cycle exists.
            if current in visited_nodes:
                return True
            
            # If not visited, add the node to the set.
            visited_nodes.add(current)
            
            # Move to the next node
            current = current.next

        # If we reach the end of the list (current becomes None), there is no cycle.
        return False