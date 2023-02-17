#Operation like 
'''Inertion
deletion 
updation'''

class Graph:
    def __init__(self,edges,vertices):
        self.adjList = [[]for _ in  range(vertices)]
        
        for (src,dest) in edges:
            self.adjList[src].append(dest)

def print(graph):
    for src in range(len(graph.adjList)):
        for dest in graph.adjList[src]: