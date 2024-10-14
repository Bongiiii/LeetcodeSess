class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        Understand:
        input - 2d array, and integer. output - boolean
        problem summary - given a 2d array determine if it's possible to carry all
         passengers with the car.

        Match:
        array

        Plan:
        -extract every first column element in each row and be adding them up and see 
        if they are less than or equal to capacity
        -you can also be checking for each row before adding to early return false 
        -we know that the inner arrays stays with length of 3, and we are concerned mostly 
        as shown by testcases if number of people taking the trip are less than or 
        equal capacity, so find the number of rows to iterate, as for columns, 
        we always want [0]
        -will need to be able to drop people off depending on where they are going
        - when people > capacity, instead of just returning false instantly, check if 
        they are dropping off before/ at the pickup spot of the people in transit

        R/E:
        s/c = O(1), will use variables to check for the people taking trip in the first place
        t/c = O(N), n being the number of rows to be traversed/ length of trips
        """
         # Step 1: Create an array to track changes at each location
        max_location = 0
        for trip in trips:
            max_location = max(max_location, trip[2])  # Get the furthest end location
        
        timeline = [0] * (max_location + 1)  # Track passengers at each location
        
        # Step 2: Track the number of passengers picked up and dropped off
        for num_passengers, start_location, end_location in trips:
            timeline[start_location] += num_passengers  # Pick up passengers
            timeline[end_location] -= num_passengers    # Drop off passengers
        
        # Step 3: Simulate the car's movement and check if capacity is exceeded
        current_passengers = 0
        for passengers_at_stop in timeline:
            current_passengers += passengers_at_stop
            if current_passengers > capacity:
                return False  # Capacity exceeded at this stop
        
        return True  # Capacity is never exceeded, all trips are possible