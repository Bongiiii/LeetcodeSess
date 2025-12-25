class Solution:
    def countAndSay(self, n: int) -> str:
        #base case
        res = "1"
        if n == 1:
            return res

        #since rle is (n-1)th
        for i in range(1, n):
            curr = res[0]
            count = 1
            new_str = ""

            for num in res[1:]:
                if num == curr:
                    count += 1
                    
                else:   
                    new_str = new_str + str(count) + curr 
                    curr = num
                    count = 1

            res = new_str + str(count) + curr

        return res