class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not n:
            return True
        flowerbed.append(0)
        count = 1
        for f in flowerbed:
            if f == 0:
                count += 1
                if count == 3:
                    n -= 1
                    if n == 0:
                        return True
                    count = 1
            else:
                count = 0
        return False
