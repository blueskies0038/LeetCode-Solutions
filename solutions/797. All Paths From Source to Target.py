class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]], curr = 0) -> List[List[int]]:
        if curr == len(graph) - 1:
            return [[len(graph) - 1]]
        return [([curr] + path) for i in graph[curr] for path in self.allPathsSourceTarget(graph, i)]
