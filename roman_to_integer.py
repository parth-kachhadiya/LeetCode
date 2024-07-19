class Solution:
    def romanToInt(self, s: str) -> int:
            reference = {
                'I' : 1,
                'V' : 5,
                'X' : 10,
                'L' : 50,
                'C' : 100,
                'D' : 500,
                'M' : 1000
            }
            numbers = [reference[i] for i in s]
            n2 = numbers.copy()
            output = 0

            for i in range(len(numbers)):
                if i == len(numbers) - 1:
                    break
                else:
                    if numbers[i] < numbers[i + 1]:
                        output += (numbers[i+1] - numbers[i])
                        n2.remove(numbers[i])
                        n2.remove(numbers[i+1])
                        
            for value in n2:
                output += value

            return output