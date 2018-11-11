class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        for c in s:
            if c != '_':
                break
        else:
            return True
        #if s == '':
        #    return True
        if not wordDict:
            return False
        return self.wordBreak(s.replace(wordDict[0], ''), wordDict[1:]) or \
                self.wordBreak(s, wordDict[1:])
