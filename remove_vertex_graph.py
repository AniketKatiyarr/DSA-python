class graph:
    def __init__(self):
        self.list={}
    
    def Pgraph(self):
        for i in self.list:
           print(i,":", self.list[i])
    def addvertex(self,vertex):
        if vertex not in self.list:
            self.list[vertex] = []
            return True
        return False
    def addedge(self,v1,v2):
          if v1 in self.list.keys() and  v2 in self.list.keys():
                self.list[v1].append(v2)
                self.list[v2].append(v1)

                return True
          return False
      
    def removeEdge(self,vertex):
        if vertex in self.list.keys():
            for other_vertex in self.list[vertex]:
                self.list[other_vertex].remove(vertex)
            del self.list[vertex]
            return True
        return False
        
    

        

mgaph = graph()
mgaph.addvertex('1')
mgaph.addvertex('2')
mgaph.addvertex('3')
mgaph.Pgraph()

#mgaph.addedge(1,2)
#mgaph.addedge(1,3)
#mgaph.addedge(3,2)
mgaph.removeEdge(1)
mgaph.Pgraph()

