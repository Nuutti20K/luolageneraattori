from objects import Vertex, Edge, Triangle

class BowyerWatson:
    def __init__(self, rooms):
        self.rooms = rooms

    def super_triangle(self):
        points = []
        for room in self.rooms:
            points.append(room.find_center().to_tuple())

        x_list = []
        y_list = []
        for point in points:
            x_list.append(point[0])
            y_list.append(point[1])

        x_max = max(x_list)
        x_min = min(x_list)
        y_max = max(y_list)
        y_min = min(y_list)

        # Etsitään pienin neliö, jonka sisään kaikki pisteet mahtuvat.
        # Tämän perusteella voidaan etsiä suorakulmaisen kolmion pisteet.

        # Wikipedian mukaan riittää, että kolmion sisään mahtuu kaikki pisteet.
        # Oikeasti kuitenkin kolmion pitäisi sisällyttää kaikkien mahdolliseten
        # kolmioiden ympäripiirrettyjen ympyröiden keskipisteet.

        # Toistaiseksi ratkasuna toimii kolmion kasvattaminen
        # mielivaltaisella tarpeeksi suurella määrällä

        square_width = max([(x_max - x_min), (y_max - y_min)])
        point_a = Vertex(x_min - square_width * 5, y_min - square_width * 5)
        point_b = Vertex(x_min + square_width * 10, y_min - square_width * 5)
        point_c = Vertex(x_min - square_width * 5, y_min + square_width * 10)

        return Triangle(point_a, point_b, point_c)

    def add_vertex(self, vertex, triangles):
        edges = []
        good_triangles = []
        for triangle in triangles:
            if triangle.inside_circumcircle(vertex):
                edges.append(Edge(triangle.v1, triangle.v2))
                edges.append(Edge(triangle.v2, triangle.v3))
                edges.append(Edge(triangle.v3, triangle.v1))
            else:
                good_triangles.append(triangle)

        edges = self.unique_edges(edges)

        for edge in edges:
            good_triangles.append(Triangle(edge.v1, edge.v2, vertex))

        return good_triangles

    def unique_edges(self, edges):
        unique_edges = []
        for i, edge1 in enumerate(edges):
            is_unique = True
            for j, edge2 in enumerate(edges):
                if edge1 == edge2 and i != j:
                    is_unique = False
            if is_unique:
                unique_edges.append(edge1)
        return unique_edges

    def triangulate(self):
        st = self.super_triangle()

        triangles = [st]
        for room in self.rooms:
            vertex = room.find_center()
            triangles = self.add_vertex(vertex, triangles)

        good_triangles = []
        for triangle in triangles:
            if (
                not (triangle.v1 == st.v1 or triangle.v1 == st.v2 or triangle.v1 == st.v3 or
                triangle.v2 == st.v1 or triangle.v2 == st.v2 or triangle.v2 == st.v3 or
                triangle.v3 == st.v1 or triangle.v3 == st.v2 or triangle.v3 == st.v3)
            ):
                good_triangles.append(triangle)

        return good_triangles
