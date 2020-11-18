class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = 0
        prev = 0
        for pos, sp in sorted(zip(position, speed), reverse=True):
            time = (target - pos)/sp
            if prev < time:
                fleet += 1
                prev = time
        return fleet
