def singleNumber(self, nums):
        #your code goes here
        dict1={}

        for ele in nums:
            if ele in dict1:
                dict1[ele] += 1

            else:
                dict1[ele] = 1

        for key,val in dict1.items():
            if val == 1:
                return key
