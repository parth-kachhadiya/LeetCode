class Solution:
    def removeElement(self, nums, val: int) -> int:
        temp_data = nums.copy()
        k = 0

        for value in temp_data:
            if val == value:
                nums.remove(value)

        for value in nums:
            if value != val:
                k += 1
        
        return k
