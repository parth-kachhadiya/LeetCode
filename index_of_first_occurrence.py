class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        i = 0
        indexer = -1

        if n > len(haystack):
            return indexer
        else:
            while (n+i) != len(haystack)+1:
                if needle == haystack[i:n+i]:
                    indexer = i
                    break
                i += 1
        
            return indexer