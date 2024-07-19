class Solution:
    def twoSum(self, nums, target):
        indexers = []

        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        indexers.append(i)
                        indexers.append(j)
                        return indexers

Obj = Solution()
print(Obj.twoSum([2,7,11,15],9))
        