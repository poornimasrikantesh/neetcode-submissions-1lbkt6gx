class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxCount=0
        res=0

        for num in nums:
            if maxCount == 0:
                res=num
            if res == num:
                maxCount += 1 
            else:
                maxCount -= 1      
        return res    