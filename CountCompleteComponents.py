# Leetcode Link: https://leetcode.com/problems/count-the-number-of-complete-components/description/
# Category: Graphs 
class Solution:
    def dfs(self, i, hm, visited, component):
        if i in visited:
            return 
        visited.add(i)
        component.append(i)
        for nextNode in hm[i]:
            self.dfs(nextNode, hm, visited, component)

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        hm = defaultdict(set)

        for edge in edges:
            u = edge[0]
            v = edge[1]
            hm[u].add(v)
            hm[v].add(u)
        
        visited = set()
        components = []
        for vertex in hm:
            if vertex not in visited: 
                c = []
                self.dfs(vertex, hm, visited, c)
                components.append(c)

        answer = 0
        

        for i in range(n):
            if i not in visited: 
                components.append([i])
        
        print(components)

        for component in components:
            if len(component) == 1:
                answer += 1
                continue
            
            component_set = set(component)
            flag = False
            for v in component:
                current_component = hm[v]
                hm[v].add(v)
                if current_component != component_set:
                    flag = True 
                    break

            if flag == False:
                answer += 1

        return answer 

            
