def isPalindrome( x: int) -> bool:
       
       rev=" "
       stringedno=(str(x))
       print(stringedno)
       if x>0:

        for i in range(len(stringedno)-1,-1,-1):
            rev+=stringedno[i]
        
        numbercontoint=int(rev)
        print(numbercontoint)
       else:
        return False

       if numbercontoint==x:
        return True
       else:
        return False
n=121

print(isPalindrome(n))
