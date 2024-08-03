class Solution:
    def isSubsequence(self, s: str, t: str):
        i,j = 0,0
        if len(s) == 0:
            return True
        else:
            while i < len(t) and j < len(s):
                if s[j] == t[i]:
                    j += 1
                i += 1

            return j == len(s)

print(Solution().isSubsequence('abc','ahbdge'))
