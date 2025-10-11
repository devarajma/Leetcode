from collections import defaultdict
class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        if n == 1:
            return True

            
        D = defaultdict(list)
        for u, v in edges:
            D[u].append(v)
            D[v].append(u)
        print(D)
        seen = set()
        stack = [source]

        while stack:
            node = stack.pop()
            for nei in D[node]:
                if nei not in seen:
                    seen.add(nei)
                    if nei == destination:
                        return True
                    stack.append(nei)
        return False




        