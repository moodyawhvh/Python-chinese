# 标题:Dijkstra 算法——从零实现单源最短路径
# 作者:Shubham Malik
# 参考资料:https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

import math
import sys

# 用于存储顶点集合,以便取出距离最小的节点


class PriorityQueue:
    # 基于最小堆
    def __init__(self):
        """
        优先队列类的构造方法。

        Examples:
        >>> priority_queue_test = PriorityQueue()
        >>> priority_queue_test.cur_size
        0
        >>> priority_queue_test.array
        []
        >>> priority_queue_test.pos
        {}
        """
        self.cur_size = 0
        self.array = []
        self.pos = {}  # 存储节点在数组中的位置

    def is_empty(self):
        """
        条件判断方法,用于确定优先队列是否为空。

        Examples:
        >>> priority_queue_test = PriorityQueue()
        >>> priority_queue_test.is_empty()
        True
        >>> priority_queue_test.insert((2, 'A'))
        >>> priority_queue_test.is_empty()
        False
        """
        return self.cur_size == 0

    def min_heapify(self, idx):
        """
        对队列数组执行堆化排序,使最小元素位于根节点。

        Examples:
        >>> priority_queue_test = PriorityQueue()
        >>> priority_queue_test.cur_size = 3
        >>> priority_queue_test.pos = {'A': 0, 'B': 1, 'C': 2}

        >>> priority_queue_test.array = [(5, 'A'), (10, 'B'), (15, 'C')]
        >>> priority_queue_test.min_heapify(0)
        >>> priority_queue_test.array
        [(5, 'A'), (10, 'B'), (15, 'C')]

        >>> priority_queue_test.array = [(10, 'A'), (5, 'B'), (15, 'C')]
        >>> priority_queue_test.min_heapify(0)
        >>> priority_queue_test.array
        [(5, 'B'), (10, 'A'), (15, 'C')]

        >>> priority_queue_test.array = [(10, 'A'), (15, 'B'), (5, 'C')]
        >>> priority_queue_test.min_heapify(0)
        >>> priority_queue_test.array
        [(5, 'C'), (15, 'B'), (10, 'A')]

        >>> priority_queue_test.array = [(10, 'A'), (5, 'B')]
        >>> priority_queue_test.cur_size = len(priority_queue_test.array)
        >>> priority_queue_test.pos = {'A': 0, 'B': 1}
        >>> priority_queue_test.min_heapify(0)
        >>> priority_queue_test.array
        [(5, 'B'), (10, 'A')]
        """
        lc = self.left(idx)
        rc = self.right(idx)
        if lc < self.cur_size and self.array[lc][0] < self.array[idx][0]:
            smallest = lc
        else:
            smallest = idx
        if rc < self.cur_size and self.array[rc][0] < self.array[smallest][0]:
            smallest = rc
        if smallest != idx:
            self.swap(idx, smallest)
            self.min_heapify(smallest)

    def insert(self, tup):
        """
        将一个节点插入优先队列。

        Examples:
        >>> priority_queue_test = PriorityQueue()
        >>> priority_queue_test.insert((10, 'A'))
        >>> priority_queue_test.array
        [(10, 'A')]
        >>> priority_queue_test.insert((15, 'B'))
        >>> priority_queue_test.array
        [(10, 'A'), (15, 'B')]
        >>> priority_queue_test.insert((5, 'C'))
        >>> priority_queue_test.array
        [(5, 'C'), (10, 'A'), (15, 'B')]
        """
        self.pos[tup[1]] = self.cur_size
        self.cur_size += 1
        self.array.append((sys.maxsize, tup[1]))
        self.decrease_key((sys.maxsize, tup[1]), tup[0])

    def extract_min(self):
        """
        移除并返回优先队列顶部的最小元素。

        Examples:
        >>> priority_queue_test = PriorityQueue()
        >>> priority_queue_test.array = [(10, 'A'), (15, 'B')]
        >>> priority_queue_test.cur_size = len(priority_queue_test.array)
        >>> priority_queue_test.pos = {'A': 0, 'B': 1}
        >>> priority_queue_test.insert((5, 'C'))
        >>> priority_queue_test.extract_min()
        'C'
        >>> priority_queue_test.array[0]
        (10, 'A')
        """
        min_node = self.array[0][1]
        self.array[0] = self.array[self.cur_size - 1]
        self.cur_size -= 1
        self.min_heapify(0)
        del self.pos[min_node]
        return min_node

    def left(self, i):
        """
        返回左孩子的索引

        Examples:
        >>> priority_queue_test = PriorityQueue()
        >>> priority_queue_test.left(0)
        1
        >>> priority_queue_test.left(1)
        3
        """
        return 2 * i + 1

    def right(self, i):
        """
        返回右孩子的索引

        Examples:
        >>> priority_queue_test = PriorityQueue()
        >>> priority_queue_test.right(0)
        2
        >>> priority_queue_test.right(1)
        4
        """
        return 2 * i + 2

    def par(self, i):
        """
        返回父节点的索引

        Examples:
        >>> priority_queue_test = PriorityQueue()
        >>> priority_queue_test.par(1)
        0
        >>> priority_queue_test.par(2)
        1
        >>> priority_queue_test.par(4)
        2
        """
        return math.floor(i / 2)

    def swap(self, i, j):
        """
        交换数组中索引 i 和 j 处的元素,并同步更新 pos{}

        Examples:
        >>> priority_queue_test = PriorityQueue()
        >>> priority_queue_test.array = [(10, 'A'), (15, 'B')]
        >>> priority_queue_test.cur_size = len(priority_queue_test.array)
        >>> priority_queue_test.pos = {'A': 0, 'B': 1}
        >>> priority_queue_test.swap(0, 1)
        >>> priority_queue_test.array
        [(15, 'B'), (10, 'A')]
        >>> priority_queue_test.pos
        {'A': 1, 'B': 0}
        """
        self.pos[self.array[i][1]] = j
        self.pos[self.array[j][1]] = i
        temp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = temp

    def decrease_key(self, tup, new_d):
        """
        减小给定元组的键值,前提是 new_d 不大于旧值。

        Examples:
        >>> priority_queue_test = PriorityQueue()
        >>> priority_queue_test.array = [(10, 'A'), (15, 'B')]
        >>> priority_queue_test.cur_size = len(priority_queue_test.array)
        >>> priority_queue_test.pos = {'A': 0, 'B': 1}
        >>> priority_queue_test.decrease_key((10, 'A'), 5)
        >>> priority_queue_test.array
        [(5, 'A'), (15, 'B')]
        """
        idx = self.pos[tup[1]]
        # 假设 new_d 不大于旧值
        self.array[idx] = (new_d, tup[1])
        while idx > 0 and self.array[self.par(idx)][0] > self.array[idx][0]:
            self.swap(idx, self.par(idx))
            idx = self.par(idx)


class Graph:
    def __init__(self, num):
        """
        Graph 类的构造方法

        Examples:
        >>> graph_test = Graph(1)
        >>> graph_test.num_nodes
        1
        >>> graph_test.dist
        [0]
        >>> graph_test.par
        [-1]
        >>> graph_test.adjList
        {}
        """
        self.adjList = {}  # 存储图:u -> (v,w)
        self.num_nodes = num  # 图中节点的数量
        # 存储与源点 vertices 的距离
        self.dist = [0] * self.num_nodes
        self.par = [-1] * self.num_nodes  # 存储路径

    def add_edge(self, u, v, w):
        """
        添加一条权重为 w 的边,从节点 u 指向 v、再从 v 指向 u:u (w)-> v、v (w) -> u

        Examples:
        >>> graph_test = Graph(1)
        >>> graph_test.add_edge(1, 2, 1)
        >>> graph_test.add_edge(2, 3, 2)
        >>> graph_test.adjList
        {1: [(2, 1)], 2: [(1, 1), (3, 2)], 3: [(2, 2)]}
        """
        # 检查 u 是否已在图中
        if u in self.adjList:
            self.adjList[u].append((v, w))
        else:
            self.adjList[u] = [(v, w)]

        # 假定为无向图
        if v in self.adjList:
            self.adjList[v].append((u, w))
        else:
            self.adjList[v] = [(u, w)]

    def show_graph(self):
        """
        展示图:u -> v(w)

        Examples:
        >>> graph_test = Graph(1)
        >>> graph_test.add_edge(1, 2, 1)
        >>> graph_test.show_graph()
        1 -> 2(1)
        2 -> 1(1)
        >>> graph_test.add_edge(2, 3, 2)
        >>> graph_test.show_graph()
        1 -> 2(1)
        2 -> 1(1) -> 3(2)
        3 -> 2(2)
        """
        for u in self.adjList:
            print(u, "->", " -> ".join(str(f"{v}({w})") for v, w in self.adjList[u]))

    def dijkstra(self, src):
        """
        Dijkstra 算法

        Examples:
        >>> graph_test = Graph(3)
        >>> graph_test.add_edge(0, 1, 2)
        >>> graph_test.add_edge(1, 2, 2)
        >>> graph_test.dijkstra(0)
        Distance from node: 0
        Node 0 has distance: 0
        Node 1 has distance: 2
        Node 2 has distance: 4
        >>> graph_test.dist
        [0, 2, 4]

        >>> graph_test = Graph(2)
        >>> graph_test.add_edge(0, 1, 2)
        >>> graph_test.dijkstra(0)
        Distance from node: 0
        Node 0 has distance: 0
        Node 1 has distance: 2
        >>> graph_test.dist
        [0, 2]

        >>> graph_test = Graph(3)
        >>> graph_test.add_edge(0, 1, 2)
        >>> graph_test.dijkstra(0)
        Distance from node: 0
        Node 0 has distance: 0
        Node 1 has distance: 2
        Node 2 has distance: 0
        >>> graph_test.dist
        [0, 2, 0]

        >>> graph_test = Graph(3)
        >>> graph_test.add_edge(0, 1, 2)
        >>> graph_test.add_edge(1, 2, 2)
        >>> graph_test.add_edge(0, 2, 1)
        >>> graph_test.dijkstra(0)
        Distance from node: 0
        Node 0 has distance: 0
        Node 1 has distance: 2
        Node 2 has distance: 1
        >>> graph_test.dist
        [0, 2, 1]

        >>> graph_test = Graph(4)
        >>> graph_test.add_edge(0, 1, 4)
        >>> graph_test.add_edge(1, 2, 2)
        >>> graph_test.add_edge(2, 3, 1)
        >>> graph_test.add_edge(0, 2, 3)
        >>> graph_test.dijkstra(0)
        Distance from node: 0
        Node 0 has distance: 0
        Node 1 has distance: 4
        Node 2 has distance: 3
        Node 3 has distance: 4
        >>> graph_test.dist
        [0, 4, 3, 4]

        >>> graph_test = Graph(4)
        >>> graph_test.add_edge(0, 1, 4)
        >>> graph_test.add_edge(1, 2, 2)
        >>> graph_test.add_edge(2, 3, 1)
        >>> graph_test.add_edge(0, 2, 7)
        >>> graph_test.dijkstra(0)
        Distance from node: 0
        Node 0 has distance: 0
        Node 1 has distance: 4
        Node 2 has distance: 6
        Node 3 has distance: 7
        >>> graph_test.dist
        [0, 4, 6, 7]
        """
        # 清空 par[] 中的旧值
        self.par = [-1] * self.num_nodes
        # src 是源节点
        self.dist[src] = 0
        q = PriorityQueue()
        q.insert((0, src))  # (与源点的距离, 节点)
        for u in self.adjList:
            if u != src:
                self.dist[u] = sys.maxsize  # 无穷大
                self.par[u] = -1

        while not q.is_empty():
            u = q.extract_min()  # 返回距源点距离最小的节点
            # 更新 u 的所有邻居的距离,
            # 若邻居原来的距离为 INFINITY,则将其压入队列 Q
            for v, w in self.adjList[u]:
                new_dist = self.dist[u] + w
                if self.dist[v] > new_dist:
                    if self.dist[v] == sys.maxsize:
                        q.insert((new_dist, v))
                    else:
                        q.decrease_key((self.dist[v], v), new_dist)
                    self.dist[v] = new_dist
                    self.par[v] = u

        # 展示从 src 出发的最短距离
        self.show_distances(src)

    def show_distances(self, src):
        """
        展示从 src 到图中其他所有节点的距离

        Examples:
        >>> graph_test = Graph(1)
        >>> graph_test.show_distances(0)
        Distance from node: 0
        Node 0 has distance: 0
        """
        print(f"Distance from node: {src}")
        for u in range(self.num_nodes):
            print(f"Node {u} has distance: {self.dist[u]}")

    def show_path(self, src, dest):
        """
        展示从 src 到 dest 的最短路径。
        警告:请在调用 dijkstra *之后*使用本方法。

        Examples:
        >>> graph_test = Graph(4)
        >>> graph_test.add_edge(0, 1, 1)
        >>> graph_test.add_edge(1, 2, 2)
        >>> graph_test.add_edge(2, 3, 3)
        >>> graph_test.dijkstra(0)
        Distance from node: 0
        Node 0 has distance: 0
        Node 1 has distance: 1
        Node 2 has distance: 3
        Node 3 has distance: 6
        >>> graph_test.show_path(0, 3)  # doctest: +NORMALIZE_WHITESPACE
        ----Path to reach 3 from 0----
        0 -> 1 -> 2 -> 3
        Total cost of path:  6
        """
        path = []
        cost = 0
        temp = dest
        # 从 dest 回溯到 src
        while self.par[temp] != -1:
            path.append(temp)
            if temp != src:
                for v, w in self.adjList[temp]:
                    if v == self.par[temp]:
                        cost += w
                        break
            temp = self.par[temp]
        path.append(src)
        path.reverse()

        print(f"----Path to reach {dest} from {src}----")
        for u in path:
            print(f"{u}", end=" ")
            if u != dest:
                print("-> ", end="")

        print("\nTotal cost of path: ", cost)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    graph = Graph(9)
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 7, 8)
    graph.add_edge(1, 2, 8)
    graph.add_edge(1, 7, 11)
    graph.add_edge(2, 3, 7)
    graph.add_edge(2, 8, 2)
    graph.add_edge(2, 5, 4)
    graph.add_edge(3, 4, 9)
    graph.add_edge(3, 5, 14)
    graph.add_edge(4, 5, 10)
    graph.add_edge(5, 6, 2)
    graph.add_edge(6, 7, 1)
    graph.add_edge(6, 8, 6)
    graph.add_edge(7, 8, 7)
    graph.show_graph()
    graph.dijkstra(0)
    graph.show_path(0, 4)

# 输出
# 0 -> 1(4) -> 7(8)
# 1 -> 0(4) -> 2(8) -> 7(11)
# 7 -> 0(8) -> 1(11) -> 6(1) -> 8(7)
# 2 -> 1(8) -> 3(7) -> 8(2) -> 5(4)
# 3 -> 2(7) -> 4(9) -> 5(14)
# 8 -> 2(2) -> 6(6) -> 7(7)
# 5 -> 2(4) -> 3(14) -> 4(10) -> 6(2)
# 4 -> 3(9) -> 5(10)
# 6 -> 5(2) -> 7(1) -> 8(6)
# Distance from node: 0
# Node 0 has distance: 0
# Node 1 has distance: 4
# Node 2 has distance: 12
# Node 3 has distance: 19
# Node 4 has distance: 21
# Node 5 has distance: 11
# Node 6 has distance: 9
# Node 7 has distance: 8
# Node 8 has distance: 14
# ----Path to reach 4 from 0----
# 0 -> 7 -> 6 -> 5 -> 4
# Total cost of path:  21
