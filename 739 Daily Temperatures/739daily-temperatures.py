class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #implemenet a monotonic stack approach
        monotonic_stack, res = [], [0] * len(temperatures)    

        for i in range(len(temperatures)-1, -1, -1):
            while monotonic_stack and temperatures[monotonic_stack[-1]] <= temperatures[i]:
                monotonic_stack.pop()

            if monotonic_stack:
                res[i] = monotonic_stack[-1] - i


            monotonic_stack.append(i)

        return res