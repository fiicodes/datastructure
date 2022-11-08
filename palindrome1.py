class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        
        s_list = list((s.replace(" ", "").lower()))

        s_updated = re.findall("[^A-Za-z0-9]", s)

        for i in s_updated:

            if i in s_list:

                s_list.remove(i)

        if ",".join(s_list[::-1]) == ",".join(s_list):
            return True
        else:
            return False


o = Solution()
print(o.isPalindrome("......a....."))
