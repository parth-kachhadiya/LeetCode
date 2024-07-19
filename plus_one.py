class Solution:
    def plusOne(self, digits):
            num = str(int(''.join([str(digit) for digit in digits])) + 1) 
            return [int(char) for char in num]