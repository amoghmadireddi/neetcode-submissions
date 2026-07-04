class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Dict = {}
        returnList = []
        for i in range(len(nums)):
            if target - nums[i] in Dict.keys():
                returnList.append(Dict[target - nums[i]])
                returnList.append(i)
                return returnList
            Dict[nums[i]] = i
        return returnList

        