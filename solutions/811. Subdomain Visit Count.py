class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visits = collections.defaultdict(int)
        for c in cpdomains:
            cp = c.replace(' ', '.').split('.')
            count = int(cp[0])
            for i in range(len(cp)-1, 0, -1):
                sub = '.'.join(cp[i:])
                visits[sub] += count
        return [str(visits[i]) + " " + i for i in visits]
