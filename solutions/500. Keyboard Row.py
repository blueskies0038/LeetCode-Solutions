class Solution:    
    def __init__(self):
        self.row1 = set("QWERTYUIOPqwertyuiop")
        self.row2 = set("ASDFGHJKLasdfghjkl")
        self.row3 = set("ZXCVBNMzxcvbnm")
    def findWords(self, words: List[str]) -> List[str]:
        return [word for word in words if self.check(word)]
    def check(self, word):
        in_row1 = all(char in self.row1 for char in word)
        in_row2 = all(char in self.row2 for char in word)
        in_row3 = all(char in self.row3 for char in word)
        return in_row1 or in_row2 or in_row3
    
