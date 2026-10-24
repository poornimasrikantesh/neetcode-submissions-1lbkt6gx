class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       if len(s) != len(t):
        return False

       hm = {}

       for c in s:
        hm[c] = hm.get(c,0)+1
       for c in t:
        hm[c] = hm.get(c,0)-1 

       for v in hm.values():
        if v!=0:
            return False
       return True     