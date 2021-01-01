class Solution:
    def countAndSay(self, n: int) -> str:
        output = '1'
        for _ in range(n - 1):
            num = output[0]
            temp = ''
            cnt = 0
            for i in output:
                if i == num:
                    cnt += 1
                else:
                    temp += str(cnt) + num
                    num = i
                    cnt = 1
            temp += str(cnt) + num
            output = temp
        return output
