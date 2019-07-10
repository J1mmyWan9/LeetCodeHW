class Solution:
     def lengthOfLongestSubstring(self, s: str) -> int:
        start=0
        end=1
        sub=""
        subs_length=[0]
        slength=len(s)
        if (slength==1):return 1 
        def has_repeat(strin: str) ->bool:
            i = 0
            while(i<len(strin)):
                if (strin[i+1:].find(strin[i:i+1])!=-1):#如果字串有重複字元回傳true 
                  return True                   
                else:
                  i+=1                    
            return False                       
        while(end<=slength):
            sub=s[start:end]
            if(has_repeat(sub)==True):#如果子字串有重複字元，-紀錄這個子字串-1的長度，接著找下一個子字串
                subs_length.append(len(sub)-1)
                start+=1
            else:
                if end==slength:
                  subs_length.append(len(sub))     
                end+=1
        return max(subs_length)
