def kruskal(graph):
    edges = graph[1]
    nodes = graph[0]
    components = [set(node) for node in list(map(lambda x: [x],nodes))]
    print(components)
    tree = []
    edges.sort(key=lambda x: x[2])
    component1 = 0
    component2 = 1
    for edge in edges:
        component1 = component2 = set()
        for component in components:
            if edge[0] in component:
                component1 = component
            elif edge[1] in component:
                component2 = component
        if component1 != component2 and component1!=set() and component2!=set():
            component1.update(component2)
            components.remove(component2)
            tree.append(edge)
        if len(tree) == len(nodes) - 1:
            break
    return tree

def prim(graph):
    edges = graph[1]
    nodes = graph[0]
    tree = []
    connected = {nodes[0]}
    while len(connected) != len(nodes):
        closest_edges = []
        for edge in edges:
            if (edge[0] in connected and edge[1] not in connected) or (edge[1] in connected and edge[0] not in connected):
                closest_edges.append(edge)
        closest_edge = sorted(closest_edges,key = lambda x: x[2])[0]
        tree.append(closest_edge)
        connected.add(closest_edge[0])
        connected.add(closest_edge[1])
    return tree