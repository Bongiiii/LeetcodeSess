class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxAmount, left, right = 0, 0, len(height) - 1

        while (left < right):
            area = (right - left) * min(height[left], height[right])
            maxAmount = max(maxAmount, area)

            if height[left] < height[right]:
                left += 1

            else:
                right -= 1

        return maxAmount


