class Solution:
    def maxSubString(self,s : str):
        uniques = []
        prev_len = 0
        for i in range(len(s)):
            while s[i] in uniques:
                uniques.pop(0)
            uniques.append(s[i])
            if len(uniques) > prev_len:
                prev_len = len(uniques)
        return prev_len

print(Solution().maxSubString("abcabcbba"))