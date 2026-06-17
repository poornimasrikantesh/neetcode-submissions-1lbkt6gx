class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1

        def isP(L, R):
            while L < R:
                if s[L] != s[R]:
                    return False
                L += 1
                R -= 1    
            return True

        while l<r:
            if s[l] != s[r]:
                return (isP(l+1,r) or isP(l,r-1))
            l += 1
            r -= 1    
        
        return True   