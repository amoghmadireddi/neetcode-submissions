class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        SFreq = {}
        TFreq = {}
        for i in range(len(s)):
            SFreq[s[i]] = 1 + SFreq.get(s[i], 0)
            TFreq[t[i]] = 1 + TFreq.get(t[i], 0)
        return SFreq == TFreq