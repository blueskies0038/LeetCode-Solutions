class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        start, max_length = 0, 0
        frequency = collections.defaultdict(int)
        
        for end in range(len(tree)):
            right_fruit = tree[end]
            frequency[right_fruit] += 1
            
            while len(frequency) > 2:
                left_fruit = tree[start]
                frequency[left_fruit] -= 1
                if frequency[left_fruit] == 0:
                    del frequency[left_fruit]
                start += 1
​
            max_length = max(max_length, end - start + 1)
    
        return max_length
