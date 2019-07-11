class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """"
        if numRows == 1 :
            return s
        else:
            x=(numRows-1)*(len(s)//(2*numRows-2))+(len(s)%(2*numRows-2))
            y=numRows
            list1= [["" for i in range(x)] for j in range(y)] 
            index = 0
            for i in range(x)
                for j in range(y)
                    if j==0:
                        if j%(2*y-1)==
                    else:       
        """
        if numRows == 1 or numRows >= len(s):
            return s

        n=numRows
        z=['']*n
        rn=list(range(0,n-1))+ list(range(n-1,0,-1))
        s_len=len(s)
        i=0        
        for l in range(s_len//(2*n-2)+1): 
            for j in range(2*n-2):
                z[rn[j]]+=s[i]
                if i == (s_len -1):
                    return "".join(z)   
                else:
                    i=i+1
