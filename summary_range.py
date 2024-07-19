class Solution:
    def summaryRanges(self, nums):
        values = []
        sub_values = []
        final_output = []

        if len(nums) == 1:
            return [f'{nums[0]}']
        else:
            for i in range(len(nums)):
                if i == (len(nums) - 1):
                    sub_values.append(nums[i])
                    values.append(sub_values)
                else:
                    if (nums[i] + 1) == nums[i + 1]:
                        sub_values.append(nums[i])
                    else:
                        sub_values.append(nums[i])
                        values.append(sub_values)
                        sub_values = []

        for rows in values:
            if len(rows) == 1:
                final_output.append(f"{rows[0]}")
            else:
                final_output.append(f"{rows[0]}->{rows[-1]}")
        
        return final_output