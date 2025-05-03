class Solution:
    def secondLargestElement(self, nums):
        lar = float('-inf')
        slar = float('-inf')

        for ele in nums:
            if ele > lar:
                slar=lar
                lar=ele

            elif ele>slar and ele!=lar:
                slar=ele

        if slar == float('-inf'):
            return -1

        return slar
