class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}

        for index, num in enumerate(nums):
            if num in mapping:
                return [mapping[num], index]
            mapping[target - num] = index
        return []