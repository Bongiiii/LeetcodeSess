class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Plan:
        - Use a stack to store indices of temperatures.
        - For each temperature, check if it is greater than the temperature at the index
          stored at the top of the stack. If it is, calculate the number of days until that warmer day.
        - If no warmer day is found for a temperature, the result will be 0 for that day.
        """
        n = len(temperatures)
        result = [0] * n  # Initialize the result array with 0s
        stack = []  # Stack to store indices of temperatures

        for i in range(n):
            # While the current temperature is greater than the temperature at the index stored in stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()  # Get the index of the previous colder temperature
                result[index] = i - index  # Calculate days to wait for a warmer day

            stack.append(i)  # Push the current index to the stack

        return result
