class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        def reverse(nums,start,end):
            while start<end:
                nums[start],nums[end]=nums[end],nums[start]
                start+=1
                end-=1

        k=k%n   # to avoid overbound condition

        # reverse the entire array first
        reverse(nums,0,n-1)

        # reverse the first k elements
        reverse(nums,0,k-1)

        # reverse the remaining k elements
        reverse(nums,k,n-1)
        
