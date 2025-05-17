def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_one=0
        count=0

        for ele in nums:
            if ele == 1:
                count += 1

            else:
                max_one = max(max_one,count)
                count = 0

        return max(max_one,count)
