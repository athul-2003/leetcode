def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        currMaxSum = nums[0]
        maxSum = nums[0]

        for i in range(1,n):
            
            currMaxSum = max(currMaxSum + nums[i], nums[i])
            maxSum = max(maxSum, currMaxSum)

        return maxSum
