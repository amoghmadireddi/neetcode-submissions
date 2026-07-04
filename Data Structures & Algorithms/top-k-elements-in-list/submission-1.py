class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = {}
        for num in nums:
            mapping[num] = mapping.get(num, 0) + 1

        freqs = [[] for _ in range(len(nums) + 1)]
        for num, freq in mapping.items():
            freqs[freq].append(num)
        returns = []
        for i in range(len(freqs) - 1, 0, -1):
            for num in freqs[i]:
                returns.append(num)
                if len(returns) == k:
                    return returns
            