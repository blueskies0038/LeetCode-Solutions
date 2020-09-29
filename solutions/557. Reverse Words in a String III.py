class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        for i in range(len(words)):
            new_word = words[i][::-1]
            words[i] = new_word
        return " ".join(words)
