def singleNumber(self, nums: List[int]) -> int:
        result=0

        for num in nums:
            result = result ^ num

        return result


"""
What is Bitwise XOR?

 - XOR (exclusive OR) is a binary operation that compares two bits:

 - In simple terms, A ^ B is 1 if A and B are different, and 0 if they are the same.

 - a ^ a = 0
 - a ^ 0 = a

 """
