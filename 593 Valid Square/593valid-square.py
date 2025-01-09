class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        """
        Understand:
        check the given 4 points make up a square
        input -4 integer array points, output - boolean

        Match:
        simulation
        geometry

        Plan:
        have a helper function that calculates distance between 2 points
        initialize a distances array to compute distances of all points
        populate the distances array using the point in the points array
        check the number of unique distances is 2, if not 2 then instantly break out of loop and return false
        unique distances are from sides and diagonals
        use the vounter module to create a dictionary and count the number distinct distances recorded
        finally return true when you have exactly 4 sides and 2 diagonals else false

        R/E:
        s/c = O(1)
        t/c = O(1)
        """
        # Helper function to check whether three points form a right angle at the first point
        def is_right_angle(point_a, point_b, point_c):
            x1, y1 = point_a
            x2, y2 = point_b
            x3, y3 = point_c
            # Calculate the squared distances between the points
            dist_ab_2 = (x1 - x2) ** 2 + (y1 - y2) ** 2
            dist_ac_2 = (x1 - x3) ** 2 + (y1 - y3) ** 2
            dist_bc_2 = (x2 - x3) ** 2 + (y2 - y3) ** 2
            # Check if the triangle formed by the three points is a right triangle
            return any([
                dist_ab_2 == dist_ac_2 and dist_ab_2 + dist_ac_2 == dist_bc_2 and dist_ab_2,
                dist_ac_2 == dist_bc_2 and dist_ac_2 + dist_bc_2 == dist_ab_2 and dist_ac_2,
                dist_ab_2 == dist_bc_2 and dist_ab_2 + dist_bc_2 == dist_ac_2 and dist_ab_2
            ])

        # Check all combinations of points to ensure all the required conditions for a valid square are met
        return (
            is_right_angle(p1, p2, p3) and
            is_right_angle(p2, p3, p4) and
            is_right_angle(p3, p1, p4) and
            is_right_angle(p1, p2, p4)
        )