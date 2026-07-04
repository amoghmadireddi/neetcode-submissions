class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        base = ord('a')
        letters = [0] * 26
        for char in s:
            letters[ord(char) - base] += 1
        for char in t:
            letters[ord(char) - base] -= 1
        for letter in letters:
            if letter != 0:
                return False
        return True

        