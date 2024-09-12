class Solution:
    def countPrimes(self, n: int) -> int:
        """
        Understand:
        input: an integer, output: integer
        prob summary: given an integer, return the count of prime numbers less than that number

        Match:
        Math
        for loop manipulation

        Plan:
        initiate a for loop from  2 upto n - 1
        base cases, o and 1 are not primes so it's zero or not considered
        prime number is a number that can only be divided by one and itself(can take 
        advantage of the fact that prime number are subsets of odd numbers with an exception
        of two so start count at 1 to count 2)
        once out of range, return count

        R/E:
        s/c = O(1), just variable assignments no extra memory usage
        t/c = O(N) n being n
        Count the number of prime numbers less than a non-negative number, n.
        Time Complexity: O(n log log n) due to Sieve of Eratosthenes
        Space Complexity: O(n) for storing the boolean prime list
        """
        if n < 2:
            return 0

        # Initialize a boolean array to track prime numbers
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

        # Start marking multiples of each number starting from 2
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, n, i):
                    is_prime[j] = False

        # Count the primes
        return sum(is_prime)