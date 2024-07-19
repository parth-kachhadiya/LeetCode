class Solution:
    def containsDuplicate(self, nums) -> bool:
        distinct_set = set(nums)    
        if len(distinct_set) == len(nums):
            return False
        else:
            return True