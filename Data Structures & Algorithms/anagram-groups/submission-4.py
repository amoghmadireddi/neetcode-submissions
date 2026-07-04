class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            counts = [0] * 26
            for letter in s:
                counts[ord(letter) - ord('a')] += 1
            result[tuple(counts)].append(s)
        return list(result.values())