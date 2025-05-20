def longestSubarray(self, arr, k):  
        # code here
        res=0
        mp={}
        prefixSum=0
        n=len(arr)
        
        for i in range(n):
            prefixSum += arr[i]
            
            if prefixSum == k:
                res = i + 1
                
            elif (prefixSum - k) in mp:
                res = max(res, i - mp[prefixSum - k])
                
            if prefixSum not in mp:
                mp[prefixSum] = i
                
        
        return res
