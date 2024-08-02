class Solution:
    def count_ones(self, n):
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count

    def countBits(self, n: int):
        opList = []
        for i in range(n+1):
            opList.append(self.count_ones(i))
        return opList
    
print(Solution().countBits(2))