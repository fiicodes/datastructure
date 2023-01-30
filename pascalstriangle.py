class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[[1]]
        #i in range of numrows-1 bcz we have already built first row
        for i in range(numRows-1):
            temp=[0]+res[-1]+[0]
            row=[]
            # j is for buildinging row
            for j in range(len(res[-1])+1):
                row.append(temp[j]+temp[j+1])
            res.append(row)
        return res