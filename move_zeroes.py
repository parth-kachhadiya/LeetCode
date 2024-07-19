class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes = []
    
        while 0 in nums:
            nums.remove(0)
            zeroes.append(0)

        nums.extend(zeroes)