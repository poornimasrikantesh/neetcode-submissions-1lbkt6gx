class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        map = {}
        for num in nums:
            map[num] = map.get(num,0)+1

        #sorted bucket
        sortMap = dict(sorted(map.items(),reverse=True))

        for num, freq in sortMap.items():
            if freq==1:
                return num
        return -1            