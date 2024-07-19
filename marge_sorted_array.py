class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
        elif n == 0:
            pass
        else:
            for i in range(n):
                nums1[m + i] = nums2[i]
        nums1.sort()
        