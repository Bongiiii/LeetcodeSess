class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        """
        Understand:
        input: string, output: boolean
        problem summary: given a string of instructions, return true if the instructions 
         are in a cycle, where at some point the robot ends up at the original position(0,0)

        Match:
        math

        Plan:
        initialize a list with initial start position as [0, 0]
        then iterate through the instructions
        then have conditionals, move based on instructions and cardinal points on the plane

        R/E:
        s/c = O(1)
        t/c = O(N)
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # N, E, S, W
        pos = [0, 0]  # Starting at the origin (0, 0)
        dir_index = 0  # Start facing north (index 0)

        for instruc in instructions:
            if instruc == 'G':
                # Move in the current direction
                pos[0] += directions[dir_index][0]
                pos[1] += directions[dir_index][1]
            elif instruc == 'L':
                # Turn left (counterclockwise)
                dir_index = (dir_index - 1) % 4
            elif instruc == 'R':
                # Turn right (clockwise)
                dir_index = (dir_index + 1) % 4

        # If the robot is back at the origin or not facing north, it is bounded
        return pos == [0, 0] or dir_index != 0

