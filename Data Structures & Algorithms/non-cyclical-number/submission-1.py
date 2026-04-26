class Solution:
    def isHappy(self, n: int) -> bool:
        
      slow=n
      fast = self.sumOfSquares(n)

      while slow != fast:
        slow=self.sumOfSquares(slow)
        fast=self.sumOfSquares(fast)
        fast=self.sumOfSquares(fast)
      return True if fast == 1 else False  

    def sumOfSquares(self, n: int) -> int:
        op = 0
        while n:
          ones = n%10
          ones = ones ** 2
          op += ones
          n = n//10
        return op  



        