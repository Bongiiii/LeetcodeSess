# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Understand:
        input: two non empty linked lists, output: linked list
        problem summary: given two linked lists with digits ordered in reverse, 
        add the two numbers and return the total as a linked list

        Match:
        linked list, math, addition, iteration

        Plan:
        - Initialize a variable to store the carry, and create a dummy node to 
        store the result.
        - Iterate through both lists, adding corresponding digits along with the carry.
        - Create a new node for each sum and append it to the result.
        - If one list is longer, continue adding its digits and the carry.
        - Finally, if there's a carry left, add it as a new node.
        """
        
        # Initialize dummy node and carry
        temp = ListNode()
        current = temp
        carry = 0
        
        # Loop while there are still digits to process in either list
        while l1 or l2 or carry:
            # Get values from the current nodes, or 0 if one list is shorter
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the total sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            
            # Create a new node with the digit and append it to the result list
            current.next = ListNode(digit)
            current = current.next
            
            # Move to the next nodes in l1 and l2
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # Return the result starting from the next node (since the first is a dummy)
        return temp.next
