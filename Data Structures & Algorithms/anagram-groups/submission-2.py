class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       output = defaultdict(list) #map character count to list of Anagrams

       for s in strs:
        count = [0] * 26 # a to z
        for c in s:
            count[ord(c) - ord('a')] += 1
        output[tuple(count)].append(s)
       return list(output.values())






