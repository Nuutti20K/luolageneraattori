from objects import Vertex, Edge, Triangle, Room

def super_triangle(rooms):
    points = []
    for room in rooms:
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

    # Etsitään pienin neliö, jonka sisään kaikki pisteet mahtuvat
    # Tämän perusteella voidaan etsiä suorakulmaisen kolmion pisteet, jonka sisään kaikki pisteet mahtuvat

    # Wikipedian mukaan riittää, että kolmion sisään mahtuu kaikki pisteet, jotta triangulaatio toimisi
    # Oikeasti kuitenkin kolmion pitäisi sisällyttää kaikkien mahdolliseten kolmioiden ympäripiirrettyjen ympyröiden keskipisteet
    # Toistaiseksi ratkasuna toimii kolmion kasvattaminen mielivaltaisella tarpeeksi suurella määrällä

    square_width = max([(x_max - x_min), (y_max - y_min)])
    point_a = Vertex(x_min - square_width * 5, y_min - square_width * 5)
    point_b = Vertex(x_min + square_width * 10, y_min - square_width * 5)
    point_c = Vertex(x_min - square_width * 5, y_min + square_width * 10)

    return Triangle(point_a, point_b, point_c)

def add_vertex(vertex, triangles):
    edges = []
    good_triangles = []
    for triangle in triangles:
        if triangle.inside_circumcircle(vertex):
            edges.append(Edge(triangle.v1, triangle.v2))
            edges.append(Edge(triangle.v2, triangle.v3))
            edges.append(Edge(triangle.v3, triangle.v1))
        else:
            good_triangles.append(triangle)

    edges = unique_edges(edges)

    for edge in edges:
        good_triangles.append(Triangle(edge.v1, edge.v2, vertex))

    return good_triangles

def bowyer_watson(rooms):
    st = super_triangle(rooms)

    triangles = [st]
    for room in rooms:
        vertex = room.find_center()
        triangles = add_vertex(vertex, triangles)

    good_triangles = []
    for triangle in triangles:
        if (
            not (triangle.v1 == st.v1 or triangle.v1 == st.v2 or triangle.v1 == st.v3 or
            triangle.v2 == st.v1 or triangle.v2 == st.v2 or triangle.v2 == st.v3 or
            triangle.v3 == st.v1 or triangle.v3 == st.v2 or triangle.v3 == st.v3)
        ):
            good_triangles.append(triangle)

    return good_triangles

def unique_edges(edges):
    unique_edges = []
    for i in range(len(edges)):
        is_unique = True
        for j in range(len(edges)):
            if edges[i] == edges[j] and i != j:
                is_unique = False
        if is_unique:
            unique_edges.append(edges[i])
    return unique_edges