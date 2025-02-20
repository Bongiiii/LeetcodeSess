class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        """
        Understand:
        input - two integers, output - integer
        clarifying question: so assumption is that this is a 12hour clock/not 24?

        Match:
        Math
        Simulation

        Plan:
        we know that a clock is 360 degrees, and every hour is 30 degrees, and within an hour
         there are 5 ticks within an hour worth 6 degrees
         6degrees for every minute that passes and for every hour = 60 minutes and we know an hour is worth 30degrees
         so 30/60 = 0.5 - for the relation between hour and minutes
        intialize two variables that will store hour hand angle and minute hand angle
        these two angles are the distance in angles of the hour hand and minute hand from 12 o'clock
        then find the absolute difference between the distance found above 
        for the final result you will need to return the minimum between the difference and 360 - difference
        since there are two angles formed between the hour hand and minute hand

        R/E:
        s/c = O(1), variable usage
        t/c = O(1), no special data structure or complex algorithm used
        """

        hhAngle, mhAngle = (hour*30) + (0.5 * minutes), 6 * minutes

        diff = abs(hhAngle - mhAngle)

        return min(diff, 360 - diff)
