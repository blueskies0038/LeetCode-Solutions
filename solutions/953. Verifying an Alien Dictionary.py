class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {}
        new_words = []
        for i, ch in enumerate(order):
            dic[ch] = i
        for w in words:
            new = []
            for c in w:
                new.append(dic[c])
            new_words.append(new)
        for w1, w2 in zip(new_words, new_words[1:]):
            if w1 > w2:
                return False
        return True
