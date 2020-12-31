class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        output = set()
        for word in words:
            val = ""
            for letter in word:
                val += morse[ord(letter) - ord('a')]
            output.add(val)
        return len(output)
