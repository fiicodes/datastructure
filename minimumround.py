class Solution:

    def minimumRounds(self, tasks: list[int]) -> int:
        from collections import Counter
                                            # Example: tasks = [2,2,3,3,2,4,4,4,4,4,4,4]

        tasks = Counter(tasks)              #          tasks = {3:2, 2:3, 4:5}

        if 1 in tasks.values(): return -1   # <-- no solution if there's a singleton

        ans = 0                             # tasks.values() = [5, 3, 2]
        for n in tasks.values():
            ans+= n//3 + bool(n%3)          # ans  = (3//3+False) + (2//3+True) + (4//3+True)
                                            #      = ( 1  +  0  ) + (  0 +  1 ) + (1   +  1 )
        return  ans                         #      = 4  <-- return

