from collections import OrderedDict

class node:
    def __init__(self,vertex=0,edges=None):
        self.vertex= vertex
        self.edges= {}

    def getvertex(self):
        return self.vertex

    def listofegdes(self):
        return self.edges.keys()

    def __str__(self):
        return str(self.vertex) + "is connected to" + str([x.vertex for x in self.edges])

    def addneighbour(self,vertex,weight=None):
        self.edges[vertex]=weight

class graph:

    def __init__(self):
        self.vertlist={}
        self.numvertex=0

    def addvertex(self,vertex):
        self.numvertex+=1
        new= node(vertex)
        self.vertlist[vertex]=new
        return new

    def __getitem__(self,n):
        return n in self.vertList

    def addedge(self,fromvertex,tovertex,weight=0):
        if fromvertex not in self.vertlist:
            self.addvertex(fromvertex)
        if tovertex not in self.vertlist:
            self.addvertex(tovertex)
        self.vertlist[fromvertex].addneighbour(self.vertlist[tovertex],weight)

    def getvertex(self,vertex):
        if vertex in self.vertlist:
            return self.vertlist[vertex]
        else:
            return None

    def getvertices(self):
        return self.vertlist.keys()

    def __iter__(self):
        return iter(self.vertlist.values())

                

g = graph()
for i in range(6):
    g.addvertex(i)
g.vertlist
g.addedge(0,1,2)
