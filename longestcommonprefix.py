from itertools import count


class Solution:
 def longestprefix(self,str1,str2):
    n1=len(str1)
    n2=len(str2)
    i=0
    j=0
    result=""
    while(i<=n1-1 and j<=n2-1):
        if (str1[i]!=str2[j]):
            break
        else:
            result+=str1[i]
        i+=1
        j+=1
    return result
 def    longestCommonPrefix(self,strs):
    prefix=strs[0]
    for i in range(1,len(strs)):
      prefix=self.longestprefix(prefix,strs[i])
    return prefix

if __name__ =="__main__":


    l=["geeksforgeeks", "geeks", "geek", "geezer"]
    ob=Solution()
    print(ob.longestCommonPrefix(l))

