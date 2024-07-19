class Solution:
    def majorityElement(self, nums) -> int:
        unique_values = list(set(nums))
        repeating = []
        for number in unique_values:
            repeating.append(nums.count(number))

        return unique_values[repeating.index(max(repeating))]