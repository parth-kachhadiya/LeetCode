class Solution:
    def getRow(self, rowIndex: int):
        result = [1]
        prev = 1

        for i in range(1,rowIndex + 1):
            value = prev * (rowIndex - i + 1) // i
            result.append(value)
            prev = value
        
        return result