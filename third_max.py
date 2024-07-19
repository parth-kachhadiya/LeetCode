class Solution:
    def thirdMax(self, nums) -> int:
        from_here = sorted(list(set(nums)))
        return from_here[-1] if len(from_here) < 3 else from_here[-3]