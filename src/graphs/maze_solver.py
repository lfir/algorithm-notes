from collections import deque


class Node():
    def __init__(self, gridposition, chr):
        self.gridposition = gridposition
        self.chr = chr
        # One entry for each possible direction: East, North, West, South.
        self.neighbors = [None, None, None, None]
        # Properties used in BFS
        self.color = "white"
        self.predecessor = None
        self.distance = 0

    def addneighbor(self, direction, neighbor):
        if neighbor is None:
            return
        self.neighbors[direction] = neighbor
        # Add self as neighbor of the node in the opposite direction.
        neighbor.neighbors[direction ^ 2] = self

def creategraph(grid):
    height = len(grid)
    width = len(grid[0])
    startnode = None
    endnode = None
    nodes = [None for _ in range(width * height)]

    for i in range(height):
        for j in range(width):
            if grid[i][j] == "W":
                continue
            node = Node((i, j), grid[i][j])
            # If there is a node left, add it to the node's list of neighbors.
            if j > 0:
                idxleftneighbor = (i * width) + j - 1
                node.addneighbor(0, nodes[idxleftneighbor])
            # If there is a node above, add it to the node's list of neighbors.
            if i > 0:
                idxupperneighbor = (i - 1) * width + j
                node.addneighbor(1, nodes[idxupperneighbor])
            if node.chr == "S": startnode = node
            if node.chr == "E": endnode = node
            idxnode = i * width + j
            nodes[idxnode] = node

    return startnode, endnode

def solvemaze(grid):
    """Returns a solution for a maze that uses the minimum number of moves possible.
    The maze is represented as a grid with the following characters
    as possible cell values:
    W: Wall
    P: Path
    S: Start position
    E: End position
    To find a solution a graph is created based on the grid and BFS is used
    to traverse it and find the shortest path between the start and end nodes.
    Preconditions: The grid contains one start and one end cell.
    Time complexity: O(V + E).
    Space complexity: O(V).
    Where V is the number of Vertices (grid's width * height) and
    E the number of Edges in the graph used for BFS.
    """
    path = []
    startnode, endnode = creategraph(grid)
    vertqueue = deque()
    vertqueue.append(startnode)
    # BFS starting from the node representing the initial position in the maze.
    while len(vertqueue) > 0:
        currentVert = vertqueue.pop()
        for nbr in currentVert.neighbors:
            if nbr is not None and nbr.color == "white":
                nbr.color = "gray"
                nbr.distance = currentVert.distance + 1
                nbr.predecessor = currentVert
                vertqueue.append(nbr)
        currentVert.color = "black"
    # Build the path from the node representing the exit position in the maze
    # to the start node, using the predecessor links.
    while endnode.predecessor is not None:
        path.append(endnode.gridposition)
        endnode = endnode.predecessor
    path.append(endnode.gridposition)

    return path
