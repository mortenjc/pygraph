#!/usr/local/bin/python3

from mjcgraph import graph
from mjcgraph import bfs
from mjcgraph import draw

import unittest

class TestBFSearch(unittest.TestCase):

    def test_test(self):
        G = graph.Graph('data/mediumG.txt')

        bfsearch = bfs.BFSearch(G, 0)
        self.assertTrue(bfsearch.has_path_to(200))

        self.assertTrue(len(bfsearch.path_to(0)) == 1)
        self.assertEqual(len(bfsearch.path_to(200)), 9)


if __name__ == '__main__':
    unittest.main()
