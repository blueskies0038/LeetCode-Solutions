class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words, letters = str.split(), list(pattern)
        if len(letters) != len(words):
            return False
        if len(letters) == 1:
            return True
        h = {}
        newPattern = []
        for letter, word in zip(letters, words):
            if word not in h.keys():
                if letter not in h.values():
                    h[word] = letter
                else:
                    h[word] = ''
            newPattern.append(h[word])
        return newPattern == letters
​
