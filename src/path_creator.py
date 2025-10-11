from objects import Vertex

class PathCreator:
    def __init__(self, edges):
        self.edges = edges

    def create_paths(self):
        paths = []
        for edge in self.edges:
            v1 = Vertex(edge[0][0], edge[0][1])
            v2 = Vertex(edge[1][0], edge[1][1])
            while v1.x != v2.x or v1.y != v2.y:
                if v1.x < v2.x:
                    v1.x += 40
                    paths.append(v1.to_tuple())
                elif v1.x > v2.x:
                    v1.x -= 40
                    paths.append(v1.to_tuple())
                if v1.y < v2.y:
                    v1.y += 40
                    paths.append(v1.to_tuple())
                elif v1.y > v2.y:
                    v1.y -= 40
                    paths.append(v1.to_tuple())
        return paths
