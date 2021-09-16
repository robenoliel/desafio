import math
import os

class GraphAnalyzer:

    def __init__(self, file):
        self.graph = []
        for line in open(file).readlines()[1:]:
            self.graph.append([float(i) for i in line[:-1].split(' ')])

        for row in self.graph.copy():
            self.graph.append([row[1], row[0], row[2]])

        self.nodes = set([row[0] for row in self.graph] + [row[1] for row in self.graph])

    def find_shortest_route_between(self,node1,node2):
        node1 = float(node1)
        node2 = float(node2)
        routes = self.find_shortest_routes_to_all(node1)
        return routes[str(node2)]
        
    def find_eccentricity(self,node):
        node = float(node)
        routes = self.find_shortest_routes_to_all(node)
        eccentricity = 0
        for node in routes:
            if routes[node]['cost'] > eccentricity:
                eccentricity = routes[node]['cost']
        return eccentricity

    def find_shortest_routes_to_all(self,node):
        node = float(node)
        visited = []
        routes = {
            str(node): 
                {
                'route' : [],
                'cost' : 0
                }
            }

        for i in range(len(self.nodes)):

            visited.append(node)
            cost_to_current = routes[str(node)]['cost']
            route_to_current = routes[str(node)]['route']
            min_cost_to_next = math.inf

            for edge in self.graph:

                if edge[0] == node:
                    
                    adjacent_node = edge[1]
                    edge_cost = edge[2]
                    if str(adjacent_node) not in routes.keys():
                        routes[str(adjacent_node)] = {
                            'route' : route_to_current + [adjacent_node],
                            'cost' : cost_to_current + edge_cost
                            }

                    if adjacent_node not in visited:
                        if edge_cost < min_cost_to_next:
                            next_node = adjacent_node
                            min_cost_to_next = edge_cost
                            
                    
                    adjacent_cost = routes[str(adjacent_node)]['cost']
                    if cost_to_current + edge_cost < adjacent_cost:
                        routes[str(adjacent_node)]['route'] = route_to_current + [adjacent_node]
                        routes[str(adjacent_node)]['cost'] = cost_to_current + edge_cost
            
            node = next_node
        return routes

    def find_minimum_spanning_tree(self):

        visited = [self.graph[0][0]]
        minimum_tree = []
        cost = 0
        
        while len(visited) < len(self.nodes):
            minimum_cost = math.inf
            for i in range(len(self.graph)):
                edge = self.graph[i]
                if edge[0] in visited and edge[1] not in visited:
                    if edge[2] < minimum_cost:
                        minimum_node = edge[1]
                        minimum_edge = edge
                        minimum_cost = edge[2]

            visited.append(minimum_node)
            minimum_tree.append(minimum_edge)
            cost += minimum_edge[2]
        
        return {'cost':cost, 'tree': minimum_tree}


    def __repr__(self):
        return str(self.graph)

graph1 = GraphAnalyzer(r'./grafos/grafo_W_1.txt')
graph2 = GraphAnalyzer(r'./grafos/grafo_W_2.txt')
graph3 = GraphAnalyzer(r'./grafos/grafo_W_3.txt')

i = 1
for graph in [graph1,graph2,graph3]:
    print(f'GRAFO {i}')
    result = graph.find_minimum_spanning_tree()
    print(f"Minimum spanning tree: {result['tree']}")
    print(f"Mininum spanning tree cost: {result['cost']}")
    print('\n ############################################### \n')
    i+=1

i = 1
for graph in [graph1,graph2,graph3]:
    destinations = [10,20,30,40,50]
    print(f'GRAFO {i}')
    for destination in destinations:
        routes = graph.find_shortest_routes_to_all(1)
        route = routes[str(float(destination))]
        print(f"Route from 1 to {destination}: {route['route']}")
        print(f"Cost from 1 to {destination}: {route['cost']}")
    print('\n ############################################### \n')
    i+=1

i = 1
for graph in [graph1,graph2,graph3]:
    nodes = [10,20,30,40,50]
    print(f'GRAFO {i}')
    for node in nodes:
        ecc = graph.find_eccentricity(node)
        print(f"Eccentricity from node {node}: {ecc}")
    print('\n ############################################### \n')
    i+=1
