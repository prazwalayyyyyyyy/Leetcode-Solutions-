class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        self.word1 = word1
        self.word2 = word2
        self.new_str = ''
        self.min_length = min(len(self.word1), len(self.word2))
        for i in range(self.min_length):
            self.new_str += self.word1[i] + self.word2[i]
        self.new_str += self.word1[self.min_length:] + self.word2[self.min_length:]
        return self.new_str

sol = Solution()
result = sol.mergeAlternately("abd", "pqrs")
print(result)