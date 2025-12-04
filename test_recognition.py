import unittest
from networkx import Graph
from recognition import admits_solution_with_two_colors


class TestRecognition(unittest.TestCase):
    def test_graph_with_less_than_three_vertices_admits_solution(self):
        for vertices in range(3):
            with self.subTest(vertices=vertices):
                g = Graph()
                g.add_nodes_from(range(vertices))
                self.assertTrue(admits_solution_with_two_colors(g))

    def test_path_graph_admits_solution(self):
        g = Graph()
        g.add_edges_from([(0, 1), (1, 2), (2, 3)])
        self.assertTrue(admits_solution_with_two_colors(g))

    def test_triangle_graph_admits_solution(self):
        g = Graph()
        g.add_edges_from([(0, 1), (1, 2), (2, 0)])
        self.assertTrue(admits_solution_with_two_colors(g))

    def test_C4_admits_solution(self):
        g = Graph()
        g.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 0)])
        self.assertTrue(admits_solution_with_two_colors(g))

    def test_K4_minus_edge_admits_solution(self):
        g = Graph()
        g.add_edges_from([(0, 1), (0, 2), (0, 3), (1, 2), (2, 3)])
        self.assertTrue(admits_solution_with_two_colors(g))

    def test_K4_does_not_admit_solution(self):
        g = Graph()
        g.add_edges_from([(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)])
        self.assertFalse(admits_solution_with_two_colors(g))


if __name__ == '__main__':
    unittest.main()