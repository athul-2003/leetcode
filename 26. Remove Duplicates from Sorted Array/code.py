class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res=1
        n=len(nums)

        for i in range(1,n):
            if nums[res-1]!=nums[i]:
                nums[res]=nums[i]
                res+=1

        return res
