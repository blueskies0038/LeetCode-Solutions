class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        setence = sentence.split(" ")
        for i in range(len(setence)):
            for j in dictionary:
                if setence[i].startswith(j):
                    setence[i] = j
        return " ".join(setence)
​
