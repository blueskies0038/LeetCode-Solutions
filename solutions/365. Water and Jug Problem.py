class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x + y < z:
            return False
        if z == x or z == y or z == x+y:
            return True
        return not z % gcd(x,y)
