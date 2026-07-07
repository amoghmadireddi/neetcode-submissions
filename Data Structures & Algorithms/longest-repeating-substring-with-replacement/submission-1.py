class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result  = 0
        left = 0
        maxf = 0
        for char in range(len(s)):
            count[s[char]] = 1 + count.get(s[char], 0)
            maxf = max(maxf, count[s[char]])

            while (char - left + 1 - maxf > k):
                count[s[left]] -= 1
                left += 1
            result = max(result, char - left + 1)
        
        return result
