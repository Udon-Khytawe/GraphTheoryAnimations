from manim import *
import networkx as nx

class SteinerTriple(Scene):
    def construct(self):
        graph = nx.Graph()
        graph.add_nodes_from([1,2,3,4,5,6,7,8,9])

        manim_graph = Graph.from_networkx(graph, layout="circular", layout_scale=2)
        
        self.play(Create(manim_graph))
        self.play(manim_graph.animate.add_edges((1,2),(2,3),(3,1)))
        self.play(manim_graph.animate.add_edges((4,5), (5,6), (6,4)))
        self.wait()
