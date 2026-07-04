class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for i, n in enumerate(nums):
            if (target - n) in mapping:
                return [mapping[target - n], i]
            mapping[n] = i