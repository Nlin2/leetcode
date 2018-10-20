class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = {"a":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".",
                "f":"..-.", "g":"--.", "h":"....", "i":"..", "j":".---",
                "k":"-.-", "l":".-..", "m":"--", "n":"-.", "o":"---",
                "p":".--.", "q":"--.-", "r":".-.", "s":"...", "t":"-", 
                "u":"..-", "v":"...-", "w":".--", "x":"-..-", "y":"-.--", 
                "z":"--.."}
        transWords = []
        for word in words:
            s = ""
            for char in word:
                s += morse[char]
            transWords.append(s)
        return len(set(transWords))
