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

        def rotate_add_edges(edge_to_add, vertex_pos, z_index, color, angle, num_rotations, about_point):
            edge_list = [] 
            for e in edge_to_add:
                p1 = vertex_pos[e[0]]
                p2 = vertex_pos[e[1]]
                l = Line(p1, p2, color=color)
                edge_list.append(l)

            edges = VGroup(*edge_list)
            edges.set_z_index(z_index)

            self.play(Create(edges, run_time=0.75))
            self.wait()

            edge_copy = edges.copy()
            for n in range(num_rotations):
                self.play(Rotate(edge_copy, angle=angle, about_point=about_point, rate_func=smooth))
                edges.add(edge_copy)
                edge_copy = edge_copy.copy()
                self.wait(0.5)

            return edges

        # first set of edges
        partition_one = rotate_add_edges([(1,2),(2,3),(3,1)], circular_pos, vertex_list[0].z_index-1, BLUE_E, 2*PI/3, 2, ORIGIN)
        partition_two = rotate_add_edges([(3,4),(4,8),(8,3)], circular_pos, vertex_list[0].z_index-1, GREEN_E, 2*PI/3, 2, ORIGIN)
        partition_three = rotate_add_edges([(3,6),(6,9),(9,3)], circular_pos, vertex_list[0].z_index-1, YELLOW_E, 2*PI/9, 2, ORIGIN)
        partition_four = rotate_add_edges([(1,6),(6,8),(8,1)], circular_pos, vertex_list[0].z_index-1, MAROON_C, 2*PI/3, 2, ORIGIN)
