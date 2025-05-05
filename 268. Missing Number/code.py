class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        sum_of_n = (n*(n+1)//2)
        sum_array=0

        for i in range(n):
            sum_array+=nums[i]

        return sum_of_n - sum_array
