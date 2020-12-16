class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        num = int(math.ceil((math.sqrt(8 * target + 1) - 1) / 2))
        diff = num * (1 + num) // 2 - target
        if diff % 2 == 0:
            return num
        else:
            return num + num % 2 + 1
