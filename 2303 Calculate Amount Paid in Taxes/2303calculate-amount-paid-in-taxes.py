class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        """still s/c = O(1), t/c = O(N)"""
        taxPaid, prev = 0, 0

        for taxBrac, percent in brackets:
            #check if amount is within the taxbrac/income bounds
            amountTaxable = max(0, min(income, taxBrac) - prev)
            #update amount to be paid in taxes
            taxPaid += amountTaxable * (percent/100)
            #reassign the prev value
            prev = taxBrac

        return taxPaid