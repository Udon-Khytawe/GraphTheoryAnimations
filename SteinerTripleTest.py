from manim import *
import networkx as nx

class SteinerTriple(Scene):
    def construct(self):
        # create a graph with nine nodes
        graph = nx.Graph()
        graph.add_nodes_from([1,2,3,4,5,6,7,8,9])
        # get the positions of the nodes
        circular_pos = nx.circular_layout(graph, dim=3, scale=2.5)

        vertex_list = []
        for v in graph.nodes:
            c = Circle(radius=0.15, color=WHITE, fill_opacity=1)
            c.move_to(circular_pos[v])
            vertex_list.append(c)
        
        verts = VGroup(*vertex_list)
        self.play(Create(verts))

        # do the first set of edges
        edge_to_add = [(1,2),(2,3),(3,1)]
        edge_list = []
        for e in edge_to_add:
            p1 = circular_pos[e[0]]
            p2 = circular_pos[e[1]]
            l = Line(p1, p2, color=BLUE_E)
            edge_list.append(l)

        edges = VGroup(*edge_list)
        edges.set_z_index(vertex_list[0].z_index-1)

        self.play(Create(edges))
        self.wait()

        edge_copy = edges.copy()
        self.play(Rotate(edge_copy, angle=2*PI/3, about_point=ORIGIN, rate_func=smooth))
        edges.add(edge_copy)
        self.wait()

        edge_copy = edge_copy.copy()
        self.play(Rotate(edge_copy, angle=2*PI/3, about_point=ORIGIN, rate_func=smooth))
        edges.add(edge_copy)
        self.wait()

        # do the first set of edges
        edge_to_add = [(3,4),(4,8),(8,3)]
        edge_list = []
        for e in edge_to_add:
            p1 = circular_pos[e[0]]
            p2 = circular_pos[e[1]]
            l = Line(p1, p2, color=GREEN_E)
            edge_list.append(l)

        edges = VGroup(*edge_list)
        edges.set_z_index(vertex_list[0].z_index-1)

        self.play(Create(edges))
        self.wait()

        edge_copy = edges.copy()
        self.play(Rotate(edge_copy, angle=2*PI/3, about_point=ORIGIN, rate_func=smooth))
        edges.add(edge_copy)
        self.wait()

        edge_copy = edge_copy.copy()
        self.play(Rotate(edge_copy, angle=2*PI/3, about_point=ORIGIN, rate_func=smooth))
        edges.add(edge_copy)
        self.wait()

        # do the next one 
        edge_to_add = [(3,6),(6,9),(9,3)]
        edge_list = []
        for e in edge_to_add:
            p1 = circular_pos[e[0]]
            p2 = circular_pos[e[1]]
            l = Line(p1, p2, color=YELLOW_E)
            edge_list.append(l)

        edges = VGroup(*edge_list)
        edges.set_z_index(vertex_list[0].z_index-1)

        self.play(Create(edges))
        self.wait()

        edge_copy = edges.copy()
        self.play(Rotate(edge_copy, angle=2*PI/9, about_point=ORIGIN, rate_func=smooth))
        edges.add(edge_copy)
        self.wait()

        edge_copy = edge_copy.copy()
        self.play(Rotate(edge_copy, angle=2*PI/9, about_point=ORIGIN, rate_func=smooth))
        edges.add(edge_copy)
        self.wait()

        # do the next one 
        edge_to_add = [(1,6),(6,8),(8,1)]
        edge_list = []
        for e in edge_to_add:
            p1 = circular_pos[e[0]]
            p2 = circular_pos[e[1]]
            l = Line(p1, p2, color=MAROON_C)
            edge_list.append(l)

        edges = VGroup(*edge_list)
        edges.set_z_index(vertex_list[0].z_index-1)

        self.play(Create(edges))
        self.wait()

        edge_copy = edges.copy()
        self.play(Rotate(edge_copy, angle=2*PI/3, about_point=ORIGIN, rate_func=smooth))
        edges.add(edge_copy)
        self.wait()

        edge_copy = edge_copy.copy()
        self.play(Rotate(edge_copy, angle=2*PI/3, about_point=ORIGIN, rate_func=smooth))
        edges.add(edge_copy)
        self.wait()
