class Solution:
    def findDisappearedNumbers(self, nums):
        for i in range(len(nums)):
            while nums[i] != (i + 1):
                correct_position = nums[i] - 1
                if nums[i] == nums[correct_position]:
                    break
                nums[i], nums[correct_position] = nums[correct_position], nums[i]

        output = []
        for i in range(len(nums)):
            if nums[i] != (i + 1):
                output.append(i+1)
        return output