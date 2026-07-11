class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
    
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [False] * n
        complete_count = 0
        
        for start in range(n):
            if visited[start]:
                continue
            
            
            stack = [start]
            visited[start] = True
            component_vertices = []
            
            while stack:
                node = stack.pop()
                component_vertices.append(node)
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
            
            
            num_vertices = len(component_vertices)
            num_edges = 0
            for node in component_vertices:
                num_edges += len(graph[node])
            num_edges = num_edges // 2  
            
            
            expected_edges = num_vertices * (num_vertices - 1) // 2
            if num_edges == expected_edges:
                complete_count += 1
        return complete_count