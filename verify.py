def dfs(dists, start, visited, nodes):
    
    nodes.append(start)
    visited[start] = True
    
    for i in range(len(dists)):
        if(dists[start][i] != 0 and (not visited[i])):
            dfs(dists, i, visited, nodes)



def verify(dists):

    visited = [False] * len(dists)
    nodes = []
    dfs(dists, 0, visited, nodes)
    if len(nodes) is len(dists):
        return True
    else:
        return False
