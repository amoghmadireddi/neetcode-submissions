class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a = 0
        b = len(numbers) - 1
        sum = numbers[a] + numbers[b]
        while(sum != target):
            if sum > target:
                b -= 1
            else:
                a += 1
            sum = numbers[a] + numbers[b]
        return [1 + a, 1 + b]
        