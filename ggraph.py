#class Graph:
#    n = 0
#    g = [0 for x in range(10) for y in range(10)]
#    
#    def __init__(self,vertices):
#        self.n  = vertices
#        
#    def display(self):
#        for i in range(self.n):
#            for j in range(self.n):
#                print(" ",self.g[i][j],end="")
#            print()
#    def addedge(self,x,y):
#            if x==y:
#                print("same node,self loop")
#            else:
#                self.g[x][y]=1
#                self.g[y][x]=1
#    
#ob = Graph(4)
#ob.addedge(0,1)
#ob.addedge(0,2)
#ob.addedge(2,1)
#ob.addedge(3,1)
#
#
#ob.display()
