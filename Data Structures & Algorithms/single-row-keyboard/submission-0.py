class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        hm = {}
        prev = 0
        result = 0

        for i in range(len(keyboard)):
            hm[keyboard[i]] = i

        for c in word:
           result +=  abs(prev - hm[c])
           prev = hm[c]
        return result   