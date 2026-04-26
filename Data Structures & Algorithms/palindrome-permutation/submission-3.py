class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        arr = [0] * 128
        oddCounter=0
        for i in range(len(s)):
            arr[ord(s[i])] += 1
            if arr[ord(s[i])] % 2 == 0:
                oddCounter -= 1
            else:
                oddCounter += 1
        return oddCounter == 1 or oddCounter == 0      
