class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        Understand:
        input: array of integers representing people's weight, integer representing one boat's 
        weight limit
        output: integer representing # of boats to be used
        prob summary: given a list with people's weights and a boat that carries 2 people of max weight
        limit, return the number of boats that can be used to carry all the people
        
        Plan:
        - Sort the array of people by weight
        - Use two pointers: one starting at the lightest person and the other at the heaviest
        - Try to pair the lightest and heaviest person if their combined weight is less than or equal to the limit
        - If they can be paired, move both pointers; if not, the heaviest person gets a boat alone
        - Repeat until all people are accounted for
        """
        # Sort the people's weights
        people.sort()
        
        # Initialize two pointers
        left, right = 0, len(people) - 1
        boats = 0
        
        # While we have people left to place in boats
        while left <= right:
            # Check if the lightest and heaviest person can fit in one boat
            if people[left] + people[right] <= limit:
                # If they can, both get in the boat, so move both pointers
                left += 1
                right -= 1
            else:
                # Otherwise, only the heaviest person gets in the boat
                right -= 1
                
            # In both cases, we use one boat
            boats += 1
        
        return boats
