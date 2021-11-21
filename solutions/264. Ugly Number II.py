class Solution:
    def nthUglyNumber(self, n: int) -> int:
        factors = [2, 3, 5]
        k = 3
        starts = [0] * k
        numbers = [1]
        for i in range(n-1):
            candidates = [factors[i]*numbers[starts[i]] for i in range(k)]
            new_num = min(candidates)
            numbers.append(new_num)
            starts = [starts[i] + (candidates[i] == new_num) for i in range(k)]
        return numbers[-1]
