class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        same = set(f for f, b in zip(fronts, backs) if f == b)
        choices = set(fronts + backs) - same
        return min(choices) if choices else 0
