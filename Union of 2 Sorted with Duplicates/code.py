class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        # code here 
        i, j = 0, 0
        union = []
        n1 = len(a)
        n2 = len(b)
        
        while i < n1 and j < n2:
            if a[i] <= b[j]:
                if len(union) == 0 or union[-1] != a[i]:
                    union.append(a[i])
                i+=1
                    
            else:
                if len(union) == 0 or union[-1] != b[j]:
                    union.append(b[j])
                j+=1
                    
        while i < n1:
            if union[-1] != a[i]:
                union.append(a[i])
            i+=1
            
        while j < n2:
            if union[-1] != b[j]:
                union.append(b[j])
            j+=1
            
        return union
