class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        default = defaultdict(list)
        for st in strs:
            count = [0] * 26
            for c in st:
                count[ord(c) - ord("a")] += 1
            
            default[tuple(count)].append(st)
        return default.values()
        