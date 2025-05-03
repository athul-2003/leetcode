class Solution:
    def check(self, nums: List[int]) -> bool:

        # Here's the idea:

        # A rotated sorted array should have at most one place 
        # where nums[i] > nums[i+1].
        # If more than one such place exists, it's not a rotated sorted array.
        
        n=len(nums)
        count=0

        for i in range(n):
            if nums[i]>nums[(i+1)%n]:
                count+=1

                if count>1:
                    return False

        return True
