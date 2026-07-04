class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def makeAnagramArray(string: str) -> List[int]:
            #O(m) of length of str
            letters = [0] * 26
            base = ord('a')
            for letter in string:
                letters[ord(letter) - base] += 1
            return letters

        mapping = collections.defaultdict(list)
        #O(mn), n strings, m is length of longest string
        for string in strs:
            mapping[tuple(makeAnagramArray(string))].append(string)
        
        return list(mapping.values())