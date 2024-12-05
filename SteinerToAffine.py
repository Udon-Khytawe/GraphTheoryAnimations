from manim import *
import networkx as nx

def create_circles(graph, pos, radius, color):
    node_list = []
    for v in graph.nodes:
        c = Circle(radius=radius, color=color, fill_opacity=1)
        c.move_to(pos[v])
        node_list.append(c)

    return node_list

def create_lines(edges, pos, color, z_index):
    edge_list = []
    for e1,e2 in edges:
        l = Line(pos[e1], pos[e2], color=color)
        l.set_z_index(z_index)
        edge_list.append(l)

    return edge_list

class SteinerToAffine(Scene):
    def construct(self):
        # create a graph with 
        graph = nx.Graph()
        graph.add_nodes_from([i for i in range(1,10)])

        # get the coordinates for the nodes
        pos = nx.circular_layout(graph, dim=3, scale=2.5)

        # create a list of circles for the nodes
        circle_list = create_circles(graph, pos, 0.15, WHITE)

        # create display the circles
        self.play(Create(VGroup(*circle_list)))
        self.wait()

        # create some lines/edges
        line_list = create_lines([(1,2),(2,3),(3,1)], pos, BLUE_E, circle_list[0].z_index)
        self.play(Create(VGroup(*line_list)))
        self.wait()
