class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        res=0
        l=0
        h=len(people)-1
        while(l<=h):
            remaining=limit-people[h]
            h-=1
            res+=1

            if (l<=h) and remaining>=people[l]:
                l+=1
        return res






