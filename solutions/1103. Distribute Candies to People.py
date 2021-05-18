class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        output = num_people * [0]
        give = 0
        while candies > 0:
            output[give % num_people] += min(candies, give + 1)
            give += 1
            candies -= give
        return output
