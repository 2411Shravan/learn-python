import networkx as nx
import matplotlib.pyplot as pyt

g=nx.Graph()

g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_egde(1,2)
g.add_egde(2,3)
g.add_egde(3,1)
print(g.nodes())
g=nx.Graph()
g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(3,1)
print(g.nodes())
print(g.edges())

nx.draw(g)
pyt.show()