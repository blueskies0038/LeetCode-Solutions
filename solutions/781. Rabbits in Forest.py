class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = Counter(answers)
        output = 0
        for k, v in counter.items():
            output += math.ceil(v / (k+1)) * (k+1)
        return output
