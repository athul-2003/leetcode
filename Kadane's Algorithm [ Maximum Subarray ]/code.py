def maxSubArraySum(self,arr):
        ##Your code here
        n=len(arr)
        maxEnding = arr[0]
        res = arr[0]
        
        for i in range(1,n):
            
            # identify the max subarray in the array
            # whether it is obtained by adding current element
            # to the previous subarray or if the current element
            # is greater than the result of 
            # adding it to the previous subarray
            maxEnding = max(maxEnding + arr[i], arr[i])
            
            # maximum subarray sum
            res = max(maxEnding, res)
            
        return res
