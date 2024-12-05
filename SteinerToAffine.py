from manim import *
import networkx as nx
import numpy as np

# def rotate_add_edges(scene, graph, edges, angle, about_point, n):
def vector_angle(A,B):
    dot = sum([a*b for a,b in zip(A,B)])
    a_mag = np.sqrt(sum([a*a for a in A]))
    b_mag = np.sqrt(sum([b*b for b in B]))
    return np.arccos(dot/(a_mag*b_mag))
    

class SteinerToAffine(Scene):
    
    def construct(self):
        def animate_add_edges(graph, edges, color):
            self.play(graph.animate.add_edges(*edges, edge_config={"stroke_color": color}))

        # assume graph in a circular layout
        def animate_rotate_add_edges(graph, edges, color, rotate_via_vertex, about_point, z_index):
            # create the new edges
            new_edges = []
            lines = []
            mod = len(graph.vertices)
            for e1,e2 in edges:
                new_e1 = (e1+rotate_via_vertex)%mod
                new_e2 = (e2+rotate_via_vertex)%mod
                new_edges.append((new_e1, new_e2))
                # also create some lines
                lines.append(Line(graph[e1].get_center(), graph[e2].get_center(), color=color, z_index=z_index))

            # create a line group
            line_group = VGroup(*lines, z_index=z_index)
            # find rotation angle
            angle = (rotate_via_vertex/mod)*2*PI
            # animate rotation
            self.play(Rotate(line_group, angle=angle, about_point=about_point), rate_func=smooth)
            self.remove(line_group)
            return new_edges

        fg = 1
        bg = -1
        num_verticies = 9
        # create a graph with num_vertices
        vertices = [i for i in range(0,num_verticies)]
        graph = Graph(vertices, [], layout="circular", layout_scale=2.5)

        self.play(Create(graph))
        self.wait()

        master_edge_config = {}
        # animate first set of edges
        edges = [(0,1),(1,2),(2,0)]
        edge_color = BLUE_E
        for e in edges:
            master_edge_config[e] = {"stroke_color": edge_color}
        animate_add_edges(graph, edges, edge_color)
        self.wait() 
        to_add = edges
        for i in range(2):
            to_add = animate_rotate_add_edges(graph, to_add, edge_color, 3, ORIGIN, graph.get_z()-1)
            for e in to_add:
                master_edge_config[e] = {"stroke_color": edge_color}
            graph.add_edges(*to_add, edge_config={"stroke_color": edge_color})
            self.wait()

        # edges = graph.edges.copy()
        # graph.remove_edges(*edges)
        # graph.add_edges(*edges, edge_config={"stroke_color":RED, "stroke_width":20})
        # self.wait()

        # animate the second set of edges
        edges = [(2,3),(3,7),(7,2)]
        edge_color = GREEN_E
        for e in edges:
            master_edge_config[e] = {"stroke_color": edge_color}
        animate_add_edges(graph, edges, edge_color)
        self.wait() 
        to_add = edges
        for i in range(2):
            to_add = animate_rotate_add_edges(graph, to_add, edge_color, 3, ORIGIN, graph.get_z()-1)
            for e in to_add:
                master_edge_config[e] = {"stroke_color": edge_color}
            graph.add_edges(*to_add, edge_config={"stroke_color": edge_color})
            self.wait()

        # animate the second set of edges
        edges = [(2,5),(5,8),(8,2)]
        edge_color = YELLOW_E
        for e in edges:
            master_edge_config[e] = {"stroke_color": edge_color}
        animate_add_edges(graph, edges, edge_color)
        self.wait() 
        to_add = edges
        for i in range(2):
            to_add = animate_rotate_add_edges(graph, to_add, edge_color, 1, ORIGIN, graph.get_z()-1)
            for e in to_add:
                master_edge_config[e] = {"stroke_color": edge_color}
            graph.add_edges(*to_add, edge_config={"stroke_color": edge_color})
            self.wait()

        # animate the second set of edges
        edges = [(0,5),(5,7),(7,0)]
        edge_color = MAROON_C
        for e in edges:
            master_edge_config[e] = {"stroke_color": edge_color}
        animate_add_edges(graph, edges, edge_color)
        self.wait() 
        to_add = edges
        for i in range(2):
            to_add = animate_rotate_add_edges(graph, to_add, edge_color, 3, ORIGIN, graph.get_z()-1)
            for e in to_add:
                master_edge_config[e] = {"stroke_color": edge_color}
            graph.add_edges(*to_add, edge_config={"stroke_color": edge_color})
            self.wait()

        # remove edges now that we have epic bold edges
        self.play(graph.animate.remove_edges((2,0),(5,3),(8,6),(8,2),(7,1),(6,0),(8,0),(6,1),(7,2),(8,1),(7,0),(6,2)))

        graph_old = graph.copy()
        to_delete = []
        # update master edge config
        for e in master_edge_config:
            if(e in graph.edges):
                master_edge_config[e]["stroke_width"] = 6
            else :
                to_delete.append(e)

        for e in to_delete:
            del master_edge_config[e]

        edges = graph.edges.copy()
        graph.remove_edges(*edges)
        graph.add_edges(*edges, edge_config=master_edge_config)

        self.play(Transform(graph_old, graph))
        self.remove(graph_old)



        # become an affine plane
        self.play(graph[2].animate.move_to([-2,2,0]), 
                  graph[1].animate.move_to([0,2,0]), 
                  graph[0].animate.move_to([2,2,0]),
                  graph[5].animate.move_to([-2,0,0]),
                  graph[4].animate.move_to([0,0,0]),
                  graph[3].animate.move_to([2,0,0]),
                  graph[8].animate.move_to([-2,-2,0]),
                  graph[7].animate.move_to([0,-2,0]),
                  graph[6].animate.move_to([2,-2,0]))
        self.wait()

        sneaky = Line(graph[3].get_center(), graph[2].get_center(), color=master_edge_config[(2,3)]["stroke_color"], stroke_width=master_edge_config[(2,3)]["stroke_width"])
        graph.remove_edges((2,3),(5,6),(0,5),(3,8))
        # self.add(sneaky)
        self.play(Transform(Line(graph[3].get_center(), graph[2].get_center(), color=master_edge_config[(2,3)]["stroke_color"], stroke_width=master_edge_config[(2,3)]["stroke_width"], z_index=graph.get_z()-1), ArcBetweenPoints(graph[3].get_center(), graph[2].get_center(),PI*1.2, color=master_edge_config[(2,3)]["stroke_color"], stroke_width=master_edge_config[(2,3)]["stroke_width"], z_index=graph.get_z()-1)),
                  Transform(Line(graph[5].get_center(), graph[6].get_center(), color=master_edge_config[(5,6)]["stroke_color"], stroke_width=master_edge_config[(5,6)]["stroke_width"], z_index=graph.get_z()-1), ArcBetweenPoints(graph[5].get_center(), graph[6].get_center(),PI*1.2, color=master_edge_config[(5,6)]["stroke_color"], stroke_width=master_edge_config[(5,6)]["stroke_width"], z_index=graph.get_z()-1)),
                  Transform(Line(graph[0].get_center(), graph[5].get_center(), color=master_edge_config[(0,5)]["stroke_color"], stroke_width=master_edge_config[(0,5)]["stroke_width"], z_index=graph.get_z()-1), ArcBetweenPoints(graph[0].get_center(), graph[5].get_center(),PI*1.2, color=master_edge_config[(0,5)]["stroke_color"], stroke_width=master_edge_config[(0,5)]["stroke_width"], z_index=graph.get_z()-1)),
                  Transform(Line(graph[8].get_center(), graph[3].get_center(), color=master_edge_config[(3,8)]["stroke_color"], stroke_width=master_edge_config[(3,8)]["stroke_width"], z_index=graph.get_z()-1), ArcBetweenPoints(graph[8].get_center(), graph[3].get_center(),PI*1.2, color=master_edge_config[(3,8)]["stroke_color"], stroke_width=master_edge_config[(3,8)]["stroke_width"], z_index=graph.get_z()-1)))

        self.wait()
