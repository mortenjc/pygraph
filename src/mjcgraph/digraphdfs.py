#!/usr/local/bin/python3

import sys

class DirectedDFSearch():
    def __init__(self, Digraph, s):
        self.marked = [False for i in range(Digraph.V)]
        self.edgeTo = [-1 for i in range(Digraph.V)]
        self.s = s
        self.V = Digraph.V
        if type(s) is int:
            self.validate_vertex(s)
            self.dfs(Digraph, s)
        else:
            for v in s:
                self.validate_vertex(v)
            for v in s:
                if not self.marked[v]:
                    self.dfs(Digraph, v);


    def validate_vertex(self, v):
        assert v >= 0 and v < self.V


    def dfs(self, Digraph, v):
        self.marked[v] = True
        for w in Digraph.adj(v):
            if not self.marked[w]:
                self.edgeTo[w] = v
                self.dfs(Digraph, w)


    def is_marked(self, v):
        return self.marked[v]


    def has_path_to(self, v):
        return self.marked[v]


    def path_to(self, v):
        path = []
        if not self.has_path_to(v):
            return path
        x = v
        while x != self.s:
            path.append(x)
            x = self.edgeTo[x]
        path.append(self.s)
        return path


    def count(self):
        return sum([1 for x in self.marked if x == True]) - 1
