class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {'1':[''], '2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':                                 ['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z'],'0':[' ']}
        combo = ['']
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(letters[digits[0]])
        for digit in digits:
            combo = [i + j for i in combo for j in letters[digit]]
        return combo