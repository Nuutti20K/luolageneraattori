from objects import Vertex, Edge

class Prims:
    def __init__(self, rooms, triangles):
        self.rooms = rooms
        self.size = len(rooms)
        self.triangles = triangles
        self.adj_matrix = [[0] * self.size for _ in range(self.size)]
        self.vertex_indexes = {}
        self.vertecies = []

    def find_edges(self):
        edges = {}

        # Tehdään sanakirja, jossa avaimina on solmut ja
        # sisältönä lista solmuista joihon avainsolmu yhdistyy

        for room in self.rooms:
            vertex = room.find_center().to_tuple()
            edges[vertex] = set()

        for triangle in self.triangles:
            edges[triangle.v1.to_tuple()].add(triangle.v2.to_tuple())
            edges[triangle.v1.to_tuple()].add(triangle.v3.to_tuple())
            edges[triangle.v2.to_tuple()].add(triangle.v1.to_tuple())
            edges[triangle.v2.to_tuple()].add(triangle.v3.to_tuple())
            edges[triangle.v3.to_tuple()].add(triangle.v1.to_tuple())
            edges[triangle.v3.to_tuple()].add(triangle.v2.to_tuple())
        return edges

    def add_edges_to_matrix(self):
        edges = self.find_edges()

        # Ineksoidaan solmut vertex_dataan vierekkyys matriisin luomisen helpottamiseksi
        # Lisäksi listataan solmut, jotta niitä voi helposti hakea indeksillä myöhemmin
        for i, edge in enumerate(edges):
            self.vertex_indexes[edge] = i
            self.vertecies.append(edge)

        # Luodaan vierekkyys matriisi, johon tallennetaan yhdistyvien solmujen indekseillä
        # niiden välinen pituus
        for v1, vertices in edges.items():
            for v2 in vertices:
                u = self.vertex_indexes[v1]
                v = self.vertex_indexes[v2]
                weight = Edge(Vertex(v1[0], v1[1]), Vertex(v2[0], v2[1])).length()
                self.adj_matrix[u][v] = weight

    def mst(self):
        in_mst = [False] * self.size
        key_values = [float("inf")] * self.size
        parents = [-1] * self.size
        key_values[0] = 0

        self.add_edges_to_matrix()

        # Etsitään key_values listasta pienin arvo ja lisätään sitä edustava solmu puuhun
        for _ in range(self.size):
            u = min((v for v in range(self.size) if not in_mst[v]), key=lambda v: key_values[v])

            in_mst[u] = True

            # Etsitään lisätyn solmun viereiset solmut, jotka eivät ole vielä puussa
            # ja kirjataan niiden paino key_values listaan ja merkataan u niiden vanhemmaksi
            for v in range(self.size):
                if 0 < self.adj_matrix[u][v] < key_values[v] and not in_mst[v]:
                    key_values[v] = self.adj_matrix[u][v]
                    parents[v] = u

        edges = []
        for i, parent in enumerate(parents):
            if parent != -1:
                edges.append((self.vertecies[i], self.vertecies[parent]))
        return edges
