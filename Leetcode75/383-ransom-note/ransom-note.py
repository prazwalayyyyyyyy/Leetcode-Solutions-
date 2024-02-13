from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashransom=defaultdict(int)


        for i in magazine:
            hashransom[i] = hashransom[i] + 1
        
        for i in ransomNote:
            if i in hashransom and hashransom[i] != 0:
                hashransom[i] = hashransom[i] -1
            else:
                return False
        return True
        