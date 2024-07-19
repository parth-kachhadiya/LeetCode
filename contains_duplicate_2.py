class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        repeters = {}

        for i in range(len(nums)):
            if nums[i] in repeters and abs(i - repeters[nums[i]]) <= k:
                return True
            repeters[nums[i]] = i
        return False