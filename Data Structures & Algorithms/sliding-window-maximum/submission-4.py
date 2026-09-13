class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque() #index 
        l = r = 0

        while r < len(nums):
            #pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l -= 1
            r += 1
        return output
            # remove left val from window


        # Brute Force
        # List of max int in every slide, outputs
        # for every i from range len(nums) - k
            # maximum = nums[i]
            # scan all i to i + k - 1, update maximum
            # append maximum into outputs

        outputs = []

        for i in range(len(nums) - k + 1):
            maximum = nums[i]
            for j in range(i , i + k):
                maximum = nums[j]
                outputs.append(maximum)
        return outputs

