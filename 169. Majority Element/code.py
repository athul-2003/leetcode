def majorityElement(self, nums: List[int]) -> int:

        dict1={}
        n=len(nums) // 2

        for ele in nums:
            if ele in dict1:
                dict1[ele] += 1
            else:
                dict1[ele] = 1

        for key,val in dict1.items():
            if val > n:
                return key
