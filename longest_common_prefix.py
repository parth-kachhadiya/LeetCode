class Solution:
    def longestCommonPrefix(self, strs) -> str:
        maxLimit = min(map(lambda x : len(x),strs))
        if len(strs) == 0:
            return 0
        elif len(strs) == 1:
            return strs[0]
        else:
            strs = sorted(strs)
            prefix = strs[0]
            ln = min(map(lambda x : len(x),strs))
            for element in strs:
                while prefix[:ln] != element[:ln]:
                    ln -= 1
                    prefix = prefix[:ln]

            return prefix