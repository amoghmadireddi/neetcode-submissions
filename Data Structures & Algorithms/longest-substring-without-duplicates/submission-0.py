class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        best = 0
        for i in range(len(s)):
            if s[i] in seen:
                while s[i] in seen:
                    seen.discard(s[i - len(seen)])
            seen.add(s[i])
            best = max(best, len(seen))
        return best