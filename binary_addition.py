class Solution:
    def addBinary_method1(self, a, b):
        '''
        Method - 1 (It may give wrong output in large number of binary) 
        such as 
                000010100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101
            +  110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011
        '''
        if a == '0' and b == '0':
            return '0'
        else:
            a = list(map(lambda val : int(val), a))
            a.reverse()
            b = list(map(lambda val : int(val), b))
            b.reverse()
            num1 = 0
            num2 = 0
            for i in range(len(a)-1,-1,-1):
                if a[i] == 1:
                    num1 += (2 ** i)
            print(num1)
            for i in range(len(b)-1,-1,-1):
                if b[i] == 1:
                    num2 += (2 ** i)
            print(num2)
            sumOfTwoNum = (num1 + num2)
            outputStr = ''

            while sumOfTwoNum != 0:
                reminder = sumOfTwoNum % 2
                sumOfTwoNum = int(sumOfTwoNum / 2)
                outputStr += f'{reminder}'
            
            return outputStr[::-1]

    '''
    - <> - <> - <> - <> - <> - <> - <> - <> - <> - <> - <Second method> - <> - <> - <> - <> - <> - <> - <> - - <> - <> -
    '''

    def operation(self,a, b, c):
        total = int(a) + int(b) + c
        if total == 0:
            return 0, '0'
        elif total == 1:
            return 0, '1'
        elif total == 2:
            return 1, '0'
        else:
            return 1, '1'

    def addBinary_method2(self, a: str, b: str) -> str:
        a, b = list(a), list(b)
        if len(a) > len(b):
            b[:0] = ['0' for _ in range(len(a)-len(b))]
        elif len(a) < len(b):
            a[:0] = ['0' for _ in range(len(b)-len(a))]

        outputStr = []
        c = 0

        for i in range(len(a)-1,-1,-1):
            c, val = self.operation(a[i], b[i], c)
            outputStr.append(val)
        if c != 0:
            outputStr.append(f'{c}')
        
        return ''.join(outputStr[::-1])
    
print(Solution().addBinary_method2('11101','111'))