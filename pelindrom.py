class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            vl = list(str(x))
            vl.reverse()
            n = int("".join(vl))
            return x == n