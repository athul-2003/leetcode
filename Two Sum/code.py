def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict1={}

        for i in range(len(nums)):
            num = nums[i]
            diff = target - num

            if diff in dict1:
                return [dict1[diff],i]

            else:
                dict1[num] = i
