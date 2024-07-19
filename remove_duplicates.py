class Solution:
    def removeDuplicates(self, nums) -> int:
        repeters = []
        temp_data = nums.copy()

        for value in temp_data:
            if value not in repeters:
                repeters.append(value)
            else:
                nums.remove(value)
        
        return len(nums)

# arr = [0,0,1,1,1,2,2,3,3,4]
# Obj = Solution()
# totalNumberOfElements = Obj.removeDuplicates(arr)
# print(totalNumberOfElements)
        