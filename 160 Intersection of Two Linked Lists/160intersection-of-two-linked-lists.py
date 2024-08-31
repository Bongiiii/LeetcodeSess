# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        Understand:
        input: two linked lists, output: intersection node val

        Match:
        two pointer
        tortoise and hare algorithm

        Plan:
        Use two pointers, one starting at headA and the other at headB.
        When one pointer reaches the end, redirect it to the head of the other list.
        If the lists intersect, the pointers will meet at the intersection node.
        """
        if not headA or not headB:
            return None
        
        pA, pB = headA, headB
        
        while pA != pB:
            # When pA reaches the end of list A, move it to the beginning of list B
            pA = pA.next if pA else headB
            
            # When pB reaches the end of list B, move it to the beginning of list A
            pB = pB.next if pB else headA
        
        # Either both are None (no intersection), or they meet at the intersection node
        return pA