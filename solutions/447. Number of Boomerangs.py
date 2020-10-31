class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        output = 0
        for i in points:
            c = collections.defaultdict(int)
            for j in points:
                c[(i[0] - j[0])**2 + (i[1] - j[1])**2] += 1
            for dist in c.values():
                output += dist*(dist-1)
        return output
