with open("hi.txt") as f:
    x = f.readlines()
    lst = []
    for i in range(len(x)):
        if i != len(x)-1:
            lst.append(x[i][:-1])
        else:
            lst.append(x[i])

#Usage of networkx for edge cutting (graph theory ewwww)


from networkx import Graph, minimum_edge_cut, connected_components
import re

graph = Graph()

for i in range(len(lst)):
    lst[i] = re.split(" |:", lst[i])
    for j in range(2, len(lst[i])):
        graph.add_edge(lst[i][0], lst[i][j])
        graph.add_edge(lst[i][j], lst[i][0])
        
hi2 = minimum_edge_cut(graph)

for h in hi2:
    graph.remove_edge(h[0], h[1])

q = connected_components(graph)
a = 1
for c in q:
    a *= len(c)
print(a)

# hi = {('fqr', 'bqp'), ('zsp', 'fhv'), ('hcd', 'cnr')}