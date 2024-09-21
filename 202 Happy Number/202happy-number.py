class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares(num):
            total = 0
            while num > 0:
                digit = num % 10
                total += digit ** 2
                num //= 10
            return total

        slow = n
        fast = sum_of_squares(n)

        # Use Floyd's cycle detection to detect if a cycle exists
        while fast != 1 and slow != fast:
            slow = sum_of_squares(slow)  # move slow by 1 step
            fast = sum_of_squares(sum_of_squares(fast))  # move fast by 2 steps

        # If fast reaches 1, n is a happy number
        return fast == 1