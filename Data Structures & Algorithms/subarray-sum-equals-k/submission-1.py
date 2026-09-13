class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = currentSum = 0
        prefixSum = {0 : 1}

        for num in nums:
            currentSum += num
            diff = currentSum - k
            result += prefixSum.get(diff, 0)
            prefixSum[currentSum] = 1 + prefixSum.get(currentSum, 0)
        
        return result