# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        U:
        input - 2 ll, output - ll

        M:
        ll manipulation
        two pointer

        P:
        edge case: when just one ll input return it, 
        inorder to achieve the sorted ll final answer
        use two pointers each at the head of both ll, and append the smallest first
        """
        temp = ListNode()
        curr = temp

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next

            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        #either of the 2 still has nodes
        curr.next = list1 or list2
        

        return temp.next
