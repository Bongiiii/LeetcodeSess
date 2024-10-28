class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        """
        Understand:
        input - array of strings, output - integer

        Match:
        array
        hashmap
        string

        Plan:
        split the string into local and domain name
        apply the processes, use delimeters, '+' and '.' and apply the necessary conditions associated with them
        Then return len of resultant set/ maybe use a dictionary to store them

        R/E:
        s/c = t/c = O(N)
        """
        email_set = set()  # Use a set to store unique emails

        for email in emails:
            local, domain = email.split('@')

            # Split local part on '+' and take the first part
            local = local.split('+')[0]

            # Remove '.' from local part
            local = local.replace('.', '')

            # Combine processed local part with domain
            fullem = local + '@' + domain

            # Add the full email to the set
            email_set.add(fullem)

        return len(email_set)  # Return the number of unique emails