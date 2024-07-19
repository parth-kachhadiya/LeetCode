class Solution:
    def generate(self, numRows: int):
        pascle = []
        prev_row = []
        for i in range(numRows):
            rw = [1] * (i + 1)
            if i >= 2:
                prev_row = pascle[i - 1]
                
                for j in range(1,i):
                    rw[j] = prev_row[j] + prev_row[j - 1]
            pascle.append(rw)

        return pascle