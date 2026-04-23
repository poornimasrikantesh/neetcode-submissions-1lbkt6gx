class Solution:
    def isHappy(self, n: int) -> bool:
        
        visit = set()
        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)

            if n==1:
                return True

        return False    

    def sumOfSquares(self, n: int) -> int:
        op = 0
        while n:
            ones = n%10
            ones = ones ** 2
            op += ones
            n = n//10

        return op



        