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


""" consider prefixSum as x, so if x-k is present then the remaining portion at end will be k

so res = max(res, i - mp[prefixSum - k ]) ,ie current index minus (x-k) index we will get the index of k
"""
