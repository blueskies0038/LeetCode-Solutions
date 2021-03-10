class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        output = []
        i, j = 0, 0
        
        while i < len(firstList) and j < len(secondList):
            first_over = firstList[i][0] >= secondList[j][0] and firstList[i][0] <= secondList[j][1]
            second_over = secondList[j][0] >= firstList[i][0] and secondList[j][0] <= firstList[i][1]
            
            if first_over or second_over:
                output.append([max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])])
        
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        
        return output
