class Solution:
    def rotateArray(self, nums, k):
        n=len(nums)

        def reverse(nums,start,end):
            while start<end:
                nums[start],nums[end]=nums[end],nums[start]
                start+=1
                end-=1

        k=k%n   # To prevent out of bound
      
        # reverse first k elements
        reverse(nums,0,k-1)

        #reverse remaining k elements
        reverse(nums,k,n-1)

        #reverse entire array 
        reverse(nums,0,n-1)
