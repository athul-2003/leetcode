class Solution:
    def largestElement(self, nums):
        lar=float('-inf')

        for ele in nums:
            if ele > lar:
                lar = ele

        return lar
