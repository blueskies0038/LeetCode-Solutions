class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        d = {}
        i = 0
        letters= "abcdefghijklmnopqrstuvwxyz"
        for letter in letters:
            d[letter] = widths[i]
            i += 1
        length = 0
        words = []
        for letter in S:
            if (length + d[letter]) > 100:
                words.append(length)
                length = d[letter]
            else:
                length += d[letter]
        return [len(words)+1, length]
