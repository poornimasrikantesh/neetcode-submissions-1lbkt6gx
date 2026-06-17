class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm = {}

        if len(s) != len(t):
            return False

        for c in s:
            hm[c] = hm.get(c,0)+1

        for d in t:
            hm[d] = hm.get(d,0)-1    

        return all(v == 0 for v in hm.values())