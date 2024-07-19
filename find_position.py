class Solution:
    def searchInsert(self, nums, target: int) -> int:
            if target in nums:
                return nums.index(target)
            elif len(nums) == 1:
                    if target >= nums[0]:
                        return 1
                    else:
                        return 0
            else:
                if target <= nums[0]:
                    return 0
                else:
                    for i in range(0,len(nums)):
                        if i == (len(nums) - 1):
                            return i + 1
                        else:
                            if target >= nums[i] and target <= nums[i + 1]:
                                return i + 1