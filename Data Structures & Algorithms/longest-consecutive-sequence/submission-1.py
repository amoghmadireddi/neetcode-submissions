class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best = 0
        if not nums:
            return 0
        seen = set(nums)
        smallest = min(seen)
        for num in seen:
            if num - 1 not in seen:
                current = num + 1
                while current in seen:
                    current += 1
                best = max(best, current - num)

        return best