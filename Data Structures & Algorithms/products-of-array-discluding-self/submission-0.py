class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1] * len(nums)
        for i in range(1, len(nums), 1):
            prefixes[i] = prefixes[i - 1] * nums[i - 1]
        print(prefixes)
        base = 1
        for i in range(len(nums) - 2, -1, -1):
            base *= nums[i + 1]
            prefixes[i] *= base
        return prefixes