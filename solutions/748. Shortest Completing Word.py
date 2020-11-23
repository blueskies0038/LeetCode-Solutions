class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
            l = [i.lower() for i in licensePlate if i.isalpha()]
            sl = list(set(l))
            rl, rrl, ll = [], [], []
            for j in words:
                c = 0
                for i in sl:
                    if l.count(i) <= j.count(i):
                        c += 1
                    else:
                        break
                if c == len(sl):
                    rl.append(j)
            for i in rl:
                ll.append(len(i))
            m = min(ll)
            for i in rl:
                if len(i) == m:
                    rrl.append(i)
            return rrl[0]
