class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        chars = [char.lower() if char not in "!?',;." else ' ' for char in paragraph]
        words = Counter(''.join(chars).split())
        output = ''
        mx = 0
        for word in words:
            if word not in banned and words[word] > mx:
                mx = words[word]
                output = word
        return output
