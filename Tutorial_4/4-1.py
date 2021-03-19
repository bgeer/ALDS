from matplotlib import pyplot as plt
import numpy as np
import time
import statistics as stats


# Een zeer generieke manier om een graaf de implementeren is er
# daarwerkelijk twee sets van te maken op basis van twee classes:
class Vertex:
    def __init__(self, identifier, data_):
        self.id = identifier
        self.data = data_

    def __eq__(self, other):  # nodig om aan een set toe te voegen
        return self.id == other.id

    def __hash__(self):  # nodig om aan een set toe te voegen
        return hash(self.id)

    def __repr__(self):
        return str(self.id) + ":" + str(self.data)


class Edge:
    def __init__(self, vertex1, vertex2, data_):
        if (vertex1.id < vertex2.id):
            self.v1 = vertex1
            self.v2 = vertex2
        else:
            self.v1 = vertex2
            self.v2 = vertex1
        self.data = data_

    def __eq__(self, other):  # nodig om aan een set toe te voegen
        return self.v1.id == other.v1.id and self.v2.id == self.v2.id

    def __hash__(self):  # nodig om aan een set toe te voegen
        return hash(str(self.v1.id) + "," + str(self.v2.id))

    def __repr__(self):
        return "(" + str(self.v1.id) + "," + str(self.v2.id) + "):" + str(self.data)


class CGraph:
    def __init__(self):
        self.V = set()
        self.E = set()

    def __str__(self):
        return "V: " + str(self.V) + "\nE: " + str(self.E)


# So, for a simple shortest path problem:
gr = CGraph()
v1 = Vertex(1, "start")
v2 = Vertex(2, "")
v3 = Vertex(3, "")
v4 = Vertex(4, "")
v5 = Vertex(5, "goal")
v6 = Vertex(6, "")
gr.V.add(v1)
gr.V.add(v2)
gr.V.add(v3)
gr.V.add(v4)
gr.V.add(v5)
gr.V.add(v6)
e1 = Edge(v1, v2, 7)
e2 = Edge(v1, v3, 9)
e3 = Edge(v1, v6, 14)
e4 = Edge(v2, v3, 10)
e5 = Edge(v2, v4, 15)
e6 = Edge(v3, v4, 11)
e7 = Edge(v3, v6, 2)
e8 = Edge(v6, v5, 9)
e9 = Edge(v4, v5, 6)
gr.E.add(e1)
gr.E.add(e2)
gr.E.add(e3)
gr.E.add(e4)
gr.E.add(e5)
gr.E.add(e6)
gr.E.add(e7)
gr.E.add(e8)
gr.E.add(e9)
print(gr)

# Is dit eigenlijk al best een langdradige manier van doen...

# Daarom kiezen mensen er vaak voor om een graaf makkelijker te respresenteren met standaard datatypes
# bijvoorbeeld: als we een dictionary maken met node identifiers als keys, en een tuple van (data, edges) als values
# met edges als een dictionary met vertex ids van de verbonden vertices als keys en de data van de edge als key
# krijgen we zoiets voor dezelfde graaf
DGraph = dict
gr2 = {1: ("start", {2: 7, 3: 9, 6: 14}),
       2: ("", {1: 7, 3: 10, 4: 15}),
       3: ("", {1: 9, 2: 10, 4: 11, 6: 2}),
       4: ("", {2: 15, 3: 11, 5: 6}),
       5: ("goal", {4: 6, 6: 9}),
       6: ("", {1: 14, 3: 2, 5: 9})
       }
print(gr2)


# Dat is makkelijker in te voeren... Maar je moet wel goed bijhouden wat ookalweer wat is.
# Bovendien heb ik er nu wat redundantie ingezet (elke node bevat de edges waaraan het verbonden zit, dus elke
# edge zit twee maal in deze datastructuur)

class Nodes:
    def __init__(self, id, node):
        self.id = id
        self.distance = 0
        self.previous = None
        self.solved = False
        self.node = node


def shortest_path_cGraph(graph, start_node, end_node):
    node_list = []
    for n in graph.V:
        new_node = Nodes(n.id, n)
        if n.id == start_node.id:
            new_node.distance = 0
            strt_node = new_node
        else:
            new_node.distance = float("inf")
        node_list.append(new_node)
    N = {strt_node}
    S = set()
    while N:
        node_min = float("inf")
        node = None
        for n in N:
            if n.distance < node_min:
                node_min = n.distance
                node = n
        N.remove(node)
        node.solved = True
        S.add(node)
        if node.id == end_node.id:
            break
        neighbours_id = dict()
        for edge in graph.E:
            if edge.v1.id == node.id:
                neighbours_id[edge.v2.id] = edge.data
            elif edge.v2.id == node.id:
                neighbours_id[edge.v1.id] = edge.data
        for m in node_list:
            if not m.solved and m.id in neighbours_id:
                if m.node not in N:
                    N.add(m)
                alt_distance = node.distance + neighbours_id[m.id]
                if m.distance > alt_distance:
                    m.distance = alt_distance
                    m.previous = node
    for i in node_list:
        if i.id == end_node.id:
            finish_distance = i.distance
            path_ids = []
            path_ids = calculate_path(i, path_ids)
            return finish_distance, path_ids


def calculate_path(node, id_list):
    id_list.append(node.id)
    if node.previous is not None:
        id_list = calculate_path(node.previous, id_list)
        return id_list
    else:
        return id_list


def shortest_path_dGraph(graph, start_node, end_node):
    node_list = dict()
    for node in graph:
        new_node = Nodes(node, graph[node])
        if graph[node] == start_node:
            new_node.distance = 0
            strt_node = new_node
        else:
            new_node.distance = float("inf")
        node_list[new_node.id] = new_node
    N = {strt_node}
    S = set()
    while N:
        node_min = float("inf")
        node = None
        for n in N:
            if n.distance < node_min:
                node_min = n.distance
                node = n
        N.remove(node)
        node.solved = True
        S.add(node)
        if "goal" == graph[node.id][0]:
            break
        for edge_key in graph[node.id][1]:
            if not node_list[edge_key].solved:
                if node_list[edge_key] not in N:
                    N.add(node_list[edge_key])
                alt_distance = node.distance + graph[node.id][1][edge_key]
                if node_list[edge_key].distance > alt_distance:
                    node_list[edge_key].distance = alt_distance
                    node_list[edge_key].previous = node
    for i in node_list:
        if "goal" == node_list[i].node[0]:
            finish_distance = node_list[i].distance
            path_ids = []
            path_ids = calculate_path(node_list[i], path_ids)
            return finish_distance, path_ids


dist, list_ids = shortest_path_cGraph(gr, v1, v5)
dist2, list_ids2 = shortest_path_dGraph(gr2, gr2[1], gr2[5])
print(dist)
print(list_ids)
print(dist2)
print(list_ids2)

time_list1 = []
time_list2 = []

for i in range(20):
    timer = time.time_ns()
    dist, list_ids = shortest_path_cGraph(gr, v1, v5)
    timer = time.time_ns() - timer
    time_list1.append(timer)
    timer = time.time_ns()
    dist2, list_ids2 = shortest_path_dGraph(gr2, gr2[1], gr2[5])
    timer = time.time_ns() - timer
    time_list2.append(timer)

print("stdev cGraph:" , stats.stdev(time_list1))
print("mean cGraph:", stats.mean(time_list1))
print(time_list1)

print("stdev dGraph:", stats.stdev(time_list2))
print("mean dGraph:", stats.mean(time_list2))
print(time_list2)