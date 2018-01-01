from adjlistgraph import graph


def dfs(graph,start):
    visited=set()
    stack=[start]
    while stack:
        vertex=stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex]-visited)
    return visited

def dfs_rec(graph,start,visited=None):
    if visited == None:
        visited=set()
        visited.add(start)
        for vertex in graph[vertex] - visited:
            dfs(graph,vertex,visited)
        return visited

def dfs_paths(graph,start,goal):
    stack=[(start,[start])]
    visited=set()

    while stack:
        (vertex,path)=stack.pop()
        for nxt in graph[vertex] - set(path):
            if nxt == goal:
                yield path + [nxt]
            else:
                stack.append(nxt,path+[nxt])
