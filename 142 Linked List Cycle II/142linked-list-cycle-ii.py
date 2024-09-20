# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Understand:
        input - linked list head, integer and output - integer
        problem summary: given a linked list head and pos, find the index where the cycle is

        Match:
        tortoise and hare algorithm
        linked list

        Plan:
        first confirm if there is a cycle(tortoise and hare algorithm) and then proceed to find the index
        if there is no cycle return -1
        if there is a cycle, iterate through the linked list and when the pointers meets, and return

        Time Complexity: O(n), where n is the number of nodes in the linked list.
        Space Complexity: O(1), since we use a constant amount of space regardless of the input size.
        """
        #edge case
        if not head:
            return None

        #detect cycle
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            #cycle found
            if slow == fast:
                break
        #no cycle
        else:
            return None

        #cycle found, now find the index/position  
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow