class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters = {}
        for letter in s:
            if letter in s_letters:
                s_letters[letter] += 1
            else:
                s_letters[letter] = 1
        for letter in t:
            if letter in s_letters:
                s_letters[letter] -= 1
            else:
                return False
        for value in s_letters.values():
            if value != 0:
                return False
        return True