class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      twoSumMap = {}

      for k, v in enumerate(nums):
        diff = target-v
        if diff in twoSumMap:
          return [twoSumMap[diff],k]
        twoSumMap[v] = k

        