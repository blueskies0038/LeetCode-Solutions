class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        j_list = [jewel for jewel in J]
        s_list = [stone for stone in S]
        both = 0
        for stone in s_list:
            if stone in j_list:
                both += 1
        return both