class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Step 1: Build the graph
        graph = {}
        for source, dest in tickets:
            if source in graph:
                graph[source].append(dest)
            else:
                graph[source] = [dest]

        # Step 2: Sort destinations lexicographically
        for key, val in graph.items():
            val.sort()

        # Step 3: Initialize the route
        route = []

        # Step 4: Define the DFS function
        def dfs(airport):
            route.append(airport)
            if len(route) == len(tickets) + 1:
                return True

            if airport in graph:
                neighbors = graph[airport][:]
                for neighbor in neighbors:
                    graph[airport].pop(0)  # Remove the first neighbor
                    if dfs(neighbor):
                        return True
                    graph[airport].append(neighbor)  # Backtrack

            route.pop()
            return False

        # Step 5: Start DFS from JFK
        dfs('JFK')
        return route