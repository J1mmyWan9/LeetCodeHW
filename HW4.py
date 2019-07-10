class Solution:
    def longestPalindrome(self, s: str) -> str:        
        for sub_length in range(len(s),0,-1):
            for start in range(0,len(s)-sub_length+1,1):
                end=start+sub_length
                sub=s[start:end]
                if sub==sub[::-1]:
                    return sub
        return""
