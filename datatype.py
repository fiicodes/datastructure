#{
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def dataTypeSize(self, str):
        datatype_size={
            "integer":4,
            "character":1,
            "long":8,
            "float":4,
            "double":8
        }
        for i,v in datatype_size.items():
            if i.lower()==str:

                ans= (v)
        return ans



        # Code here

#{
 # Driver Code Starts.
if __name__ == '__main__':
    t = int(input ())
    for _ in range (t):
        str = input()
        ob = Solution()
        res = ob.dataTypeSize(str)
        print(res)
# } Driver Code Ends