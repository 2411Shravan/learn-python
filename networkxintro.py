# import networkx as nx
# from networkx import networkx as nx


g=nx.Graph()
g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)
g.add_edge(1,2)
g.add_egde(2,3)
g.add_egde(3,4)
g.add_egde(4,1)
print(g.nodes())