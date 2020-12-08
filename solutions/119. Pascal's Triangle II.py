class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans=[[1]*i for i in range(1,rowIndex+2)]
        for i in range(1,rowIndex):
            for j in range(len(ans[i])-1):
                ans[i+1][j+1]=ans[i][j]+ans[i][j+1]
        return ans[rowIndex]
