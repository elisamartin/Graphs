"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # check if at least 2 vertices
        if v1 in self.vertices and v2 in self.vertices:
            # add the v2 to the vertices at v1
            self.vertices[v1].add(v2)
        else:
            raise IndexError("The vertex does not exist")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create an empty queue enqueue the staring node ID
        q = Queue()
        q.enqueue(starting_vertex)
        # Create a Set to store the visited nodes
        visited = set()
        # While the queue is not empty
        while q.size() > 0:
            # Dequeue the first node
            v = q.dequeue()
            # if the current node has not been visited
            if v not in visited:
                # mark as visited. print v and add v to visited set
                # print(v)
                visited.add(v)

                # then add all of it's neighbours to the back of the queue
                for next_node in self.vertices[v]:
                    q.enqueue(next_node)
        print('\nbft -> ', visited)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create an empty stack push the staring node ID
        s = Stack()
        s.push(starting_vertex)
        # Create a Set to store the visited nodes
        visited = set()
        print('\ndft:')
        # While the queue is not empty
        while s.size() > 0:
            # pop the first node
            v = s.pop()
            # if the current node has not been visited
            if v not in visited:
                # mark as visited. print v and add v to visited set
                print(v)
                visited.add(v)
                # then add all of it's neighbours onto the stack
                for next_node in self.vertices[v]:
                    s.push(next_node)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        print(starting_vertex)
        visited.add(starting_vertex)
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)
                

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        q = Queue()
        q.enqueue([starting_vertex])
        # Create a Set to store the visited nodes
        visited = set()
        # While the queue is not empty
        while q.size() > 0:
            # Dequeue the first node
            path = q.dequeue()  # TODO rework for path
            v = path[-1]
            # if the current node has not been visited
            if v not in visited:
                # TODO rework for path
                if v == destination_vertex:
                    return path
                # mark as visited. print v and add v to visited set
                visited.add(v)
                # then add all of it's neighbours to the back of the queue
                for next_node in self.vertices[v]:
                    new_path = path.copy()
                    new_path.append(next_node)
                    print(f"{v} - {new_path}")
                    q.enqueue(new_path)
        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        visited = set()
        s.push(starting_vertex)
        while destination_vertex not in visited:
            v = s.pop()
            if v not in visited:
                visited.add(v)
                print(v)
                if v is not None:
                    for neighbor in self.vertices[v]:
                        s.push(neighbor)
                else:
                    return print("they don't connect")


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    # graph.add_vertex("A")
    # graph.add_vertex("B")
    # graph.add_vertex("C")
    # graph.add_vertex("D")
    # graph.add_vertex("E")
    # graph.add_vertex("F")
    # graph.add_vertex("G")
    # graph.add_edge("E", "C")
    # graph.add_edge("F", "C")
    # graph.add_edge("G", "A")
    # graph.add_edge("D", "G")
    # graph.add_edge("A", "B")
    # graph.add_edge("G", "F")
    # graph.add_edge("B", "D")
    # graph.add_edge("C", "E")
    # graph.add_edge("B", "C")
    # graph.add_edge("D", "F")

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print('\ngraph.vertices ->', graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('\ndft_recursive')
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print('\nbfs(1, 6)')
    graph.bfs(1, 6)

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print('\ndfs(1, 6)')
    graph.dfs(1, 6)
