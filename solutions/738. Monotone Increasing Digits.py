class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        if n < 10: 
            return n
        arr = [int(i) for i in str(n)]
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                while i > 0 and arr[i] <= arr[i - 1]:
                    i -= 1
                arr[i] -= 1
                for j in range(i + 1, len(arr)):
                    arr[j] = 9
                output =  int(''.join([str(k) for k in arr]))
                return output
        return n
