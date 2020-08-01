class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.lower() or word == word.upper():
            return True
        for letter in word[1:]:
            if letter != letter.lower():
                return False
        return True
