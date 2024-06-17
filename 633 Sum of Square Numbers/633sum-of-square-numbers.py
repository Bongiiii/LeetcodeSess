class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # use iteration
        ptr1, ptr2 = 0, int(sqrt(c))

        while ptr1<=ptr2:
            sum_sqr = (ptr1 * ptr1) + (ptr2 * ptr2)

            if sum_sqr == c:
                return True
            elif sum_sqr < c:
                ptr1 += 1
            else:
                ptr2 -= 1

        return False
        