class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        returns = []
        for index, num in enumerate(nums):
            if num > 0:
                break
            if index > 0 and num == nums[index - 1]:
                continue
            left = index + 1
            right = len(nums) - 1
            while left < right:
                total = num + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    returns.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1
        return returns