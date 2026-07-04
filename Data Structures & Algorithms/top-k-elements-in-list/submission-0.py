class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for n in range(len(nums) + 1)]
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, c in count.items():
            freq[c].append(num)
        
        returnarray = []

        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                returnarray.append(n)
            if len(returnarray) == k:
                return returnarray

        