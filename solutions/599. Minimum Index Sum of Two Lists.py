class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = {}
        for i in list1:
            if i in list2:
                common[i] = list1.index(i) + list2.index(i)
        return [x for x in common if common[x] == min(common.values())]
