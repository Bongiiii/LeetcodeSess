class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Optimized Plan:
        - Use binary search to partition the smaller array `nums1`.
        - Ensure that the maximum of the left partition is smaller than the minimum of the right partition.
        - Return the median based on the partition.

        R/E:
        s/c = O(1), no extra space is used beyond constant variables.
        t/c = O(log(min(m, n))), where m and n are the lengths of the two arrays.
        """

        # Ensure nums1 is the smaller array to apply binary search
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            partition1 = (left + right) // 2
            partition2 = (m + n + 1) // 2 - partition1

            # Edge cases: handling out of bounds
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]

            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]

            # Check if the partitions are correct
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # Found the correct partition
                if (m + n) % 2 == 0:  # Even total number of elements
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
                else:  # Odd total number of elements
                    return max(maxLeft1, maxLeft2)
            elif maxLeft1 > minRight2:
                # Move towards the left in nums1
                right = partition1 - 1
            else:
                # Move towards the right in nums1
                left = partition1 + 1

        raise ValueError("Input arrays are not sorted")
