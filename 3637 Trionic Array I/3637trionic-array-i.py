class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        """
        U:
        input - integer array, output - boolean
        prob summary: determine if the given array is trionic, strictly 
        increasing till p, decreasing from p to q and increases again
         at q to end of array

        M:
        array manipulation

        P:
        obviously we cant sort sooo cant even be asked as a clarifying qn

        brute force:
        do like 2 for loop sweeps 
        first sweep to keep track of indices where the strictly increase/
         decrease is seen

        second sweep is checking if the elements at indices are
         sharp increase then decline

        cleaned up brute force:
        have an array that will keep track of indices where increase
         ends and decline ends and increase ends again
        so first for loop enumerates so that we can easily keep track of 

        #instead of array to keep track of the 3, we always know
         that n-1 is last element and we just need to find p and q,
          so have pointers and traverse
         and look for p and q, and q cannot be n-1
        and then treat, p,q,n-1 as treenodes...a bst trees by definition,
         root is elem at q, and elem at p is less than elem at q
          and elem at n-1 is greater than  root elem

        optimal approach, try finding the mid point, the pinacle point(hills and valleys), and check if everything to left of it is less and check everything to the right is less and the last elem is higher than mid pinacle 


        I:
        R:
        s/c = O(1), using pointers
        t/c = O(N)
        E:

        """
        n = len(nums)

        p = 0

        while p < n - 2 and nums[p] < nums[p + 1]:
            p += 1

        if p == 0:
            return False

        q = p

        while q < n - 1 and nums[q] > nums[q + 1]:
            q += 1

        if q == p or q == n - 1:
            return False

        r = q

        while r < n - 1 and nums[r] < nums[r + 1]:
            r += 1

        return r == n - 1
