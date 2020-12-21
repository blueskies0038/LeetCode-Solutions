class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) < 2:
            return False
        h = collections.defaultdict(int)
        for card in deck:
            h[card] += 1
        counts = [count for count in h.values()]
        return self.gcd(counts) > 1
    
    def gcd(self, arr: List[int]) -> int:
        gcd = arr[0]
        for i in arr[1:]:
            gcd = self.find_gcd(gcd, i)
            if gcd == 1:
                return 1
        return gcd
    
    def find_gcd(self, num1: int, num2: int)->int:
        if not num2:
             return num1
        return self.find_gcd(num2, num1 % num2)
