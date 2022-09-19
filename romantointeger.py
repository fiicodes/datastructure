class romancode:
    def converttoint(self,s:str) -> int:
        r={"I":1,"V":5,"X":10,"C":100,"M":1000,"D":500,"L":50}
        result=0
        for i in range(len(s)):
            if i+1<len(s) and (r[s[i]]<r[s[i+1]]):
                result-=r[s[i]]
            else:
                result+=r[s[i]]
        return result    
o=romancode()
print(o.converttoint(s="LVIII"))