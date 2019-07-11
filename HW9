class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for jew in list(J):
            while S.find(jew)!=-1:
                S=S.replace(jew,"",1)
                count += 1
        return count        
