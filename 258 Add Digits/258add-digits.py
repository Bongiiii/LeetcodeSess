class Solution:
    def addDigits(self, num: int) -> int:
        if num>0:
            last = num % 10
            num = num // 10
            new_num = num + last
            while new_num>9:
                end = new_num % 10
                new_num = new_num // 10
                new_num = new_num + end
            return new_num


        return num

