class Solution:
    def singleNumber(self, nums) -> int:
        for number in nums:
            if nums.count(number) == 1:
                return number