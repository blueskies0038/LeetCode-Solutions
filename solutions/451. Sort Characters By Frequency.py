class Solution:
    def frequencySort(self, s: str) -> str:
        letters = {}
        output = ''
        
        for letter in s: 
            if letter not in letters: 
                letters[letter] = 1
            else:
                letters[letter] += 1
                
        sorted_letters = sorted(letters.items(), key=lambda x:x[1], reverse=True)
        
        for s_letter in sorted_letters: 
            l, num = s_letter[0], s_letter[1]
            freq = l * num
            output += freq
            
        return output
