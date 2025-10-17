# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Bruteforce:
        extract points and place in array and then two pointer palindrome checker
        s/c = t/c = O(N)

        optimal:
        find the middle node, reverse second half of linked list
         and then check for palindrome
        R/E - s/c = O(1), t/c = O(N)
        """
        slow = fast = head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        #mid is usually slow.val / slow fpr 2-->1
        prev, temp = None, slow #assign the mid val as your start when
        # reversing the new ll

        while temp:
            new_node = temp.next
            temp.next = prev
            prev = temp
            temp = new_node

        #start using prev node/reversed head to check palindromes with original ll
        while prev:
            if prev.val != head.val:
                return False

            prev, head = prev.next, head.next

        return True  