class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
       
    
        
    
    #     if sorted(s)==sorted(t):
            
    #         return True
    #     else:
    #         return False


    def isAnagram(self, s: str, t: str) -> bool:
        s_d=dict()
        t_d=dict()
        count=0
        if len(s)!=len(t):
            return False
        for i in (s):
            s_d[i]=count+1
        print(s_d)

        
ob=Solution()
(ob.isAnagram("anagram","naaram"))