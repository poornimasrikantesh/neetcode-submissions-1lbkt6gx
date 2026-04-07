class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hm = {}

        for i in range(len(nums2)):
            hm[nums2[i]] = i

        ans = [0]* len(nums1)
        for i in range(len(nums1)):
            ans[i] = hm[nums1[i]]
        return ans        


