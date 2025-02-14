from collections import defaultdict
from typing import List


"""
    Understand:
    input: array of arrays of strings, output: array of arrays of strings

    Match:
    graphs - bilateral
    array manipulation
    Union find

    Plan:
    create a helper function that finds commonalities in emails 
    then stores them in an array
    iterate through input array till you visit all elements
    and return output array with merged accounts

    R/E:
    s/c = O(N)
    t/c = O(NlogN)
    """

class UnionFind:
    def __init__(self):
        self.parent = {}  # Maps an email to its parent email
        self.rank = {}    # Used for union by rank

    def find(self, email):
        # Path compression
        if self.parent[email] != email:
            self.parent[email] = self.find(self.parent[email])
        return self.parent[email]

    def union(self, email1, email2):
        root1, root2 = self.find(email1), self.find(email2)
        if root1 != root2:
            # Union by rank
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        email_to_name = {}

        # Step 1: Build Union-Find Structure
        for account in accounts:
            name = account[0]
            first_email = account[1]

            for email in account[1:]:
                if email not in uf.parent:
                    uf.parent[email] = email  # Initialize parent
                    uf.rank[email] = 0  # Initialize rank
                uf.union(first_email, email)  # Connect all emails in the account
                email_to_name[email] = name   # Map email to name

        # Step 2: Group Emails by Their Root
        merged_accounts = defaultdict(list)
        for email in email_to_name:
            root = uf.find(email)  # Find the representative (root) of this email group
            merged_accounts[root].append(email)

        # Step 3: Construct Output
        output = []
        for root_email, emails in merged_accounts.items():
            output.append([email_to_name[root_email]] + sorted(emails))  # Attach name and sort emails

        return output

        