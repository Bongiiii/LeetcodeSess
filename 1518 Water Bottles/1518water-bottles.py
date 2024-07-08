class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        '''
        with 9bottles and 3that are equivalent to a bottle in the market... so we assume 
        you drink all the initial 9, so have a variable to keep track of drank bottles and variable enpty which is found by
        then divide the 9 empty by the exchange rate at market which is 9//3=3 and 9%3 so you can get 3 bottles to drink
        then add to drank which is now 12, then divide the 3 you just drank 3//3 and you get 1 water bottle 
        and add to drank =13 and that cant be exchanged so breakout of the loop
        '''
        drink, empty = numBottles, numBottles

        while (empty >= numExchange):

            drink += (empty // numExchange)
            empty = (empty // numExchange) + (empty % numExchange)

        return drink
        