class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        if buckets <= 1:
            return 0
        rounds = minutesToTest/minutesToDie + 1
        p = rounds
        x = 1
        while p < buckets:
            x += 1
            p *= rounds
        return x
    
