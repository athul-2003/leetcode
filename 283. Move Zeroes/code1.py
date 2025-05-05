class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res=0
        n=len(nums)
        for i in range(n):
            if nums[i]!=0:
                nums[res]=nums[i]
                res+=1

        while (res<n):
            nums[res]=0
            res+=1
