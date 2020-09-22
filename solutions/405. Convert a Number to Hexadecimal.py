class Solution:
    def toHex(self, num: int) -> str:
        hex_dict = {10 : 'a',11 : 'b',12 : 'c',13 : 'd',14 : 'e',15 : 'f'}
        if num == 0:
            return "0"
        if num < 0:
            num += pow(2,32)
        output = []
        while num != 0:
            rem = num % 16
            if rem in hex_dict:
                output.append(hex_dict[rem])
            else:
                output.append(str(rem))
            num = int(num/16)
        
        return ''.join(reversed(output))
