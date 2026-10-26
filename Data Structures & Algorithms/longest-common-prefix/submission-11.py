class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]
        for i in range(len(strs[0])):
            for string in strs:
                if i == len(string) or string[i] != first[i]:
                    return strs[0][:i]
        return strs[0]                