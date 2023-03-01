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

mgaph = graph()
mgaph.addvertex('A')
mgaph.Pgraph()
