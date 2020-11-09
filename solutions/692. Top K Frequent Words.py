class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = {}
        for word in words:
            if word in count:
                count[word] += 1
            else:
                count[word] =  1
        sort = sorted(count, key=lambda x: (-count[x], x))
        return sort[0:k]
