class Solution:
    def missingNumber(self, nums) -> int:
        nums.sort()
        if len(nums) == 1:
            return 1 if nums[0] == 0 else 0
        else:
            values = [nums[i] - 1 for i in range(1,len(nums)) if nums[i] - nums[i - 1] != 1]
            if values:
                return values[0]
            else:
                if min(nums) == 1:
                    return 0
                else:
                    return len(nums)