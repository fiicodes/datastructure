class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
       
    
        
    
    #     if sorted(s)==sorted(t):
            
    #         return True
    #     else:
    #         return False


    def isAnagram(self, s: str, t: str) -> bool:
        s_d={}
        t_d={}
       
        if len(s)!=len(t):
            return False
       
        for i in (s):
            if i in s_d:
            
                s_d[i]+=1
            else:
                s_d[i]=1
            if i in t_d:
            
                t_d[i]+=1
            else:
                t_d[i]=1
        if s_d==t_d:
            return True 
        else:
            return False

        
ob=Solution()
print((ob.isAnagram("cat","ngaram")))