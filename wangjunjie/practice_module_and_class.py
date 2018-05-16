# -*- coding: utf-8 -*-
'''
@author: wangjunjie
@contact: wangjunjie_93@163.com
@file: practice_module_and_class.py
@time: 2018\5\7 0007 21:47
@desc: 模块和类
'''

'''安装requests并使用，引入时候给requests包使用别名。使用requests包调用github API获取返回值
  + github API https://developer.github.com/v3/
'''
import requests as res  # 引入时候给requests包使用别名
from collections import OrderedDict

r = res.get('https://developer.github.com/v3/')
print(r.text)

'''堆栈和队列。编写一个类，定义一个能够同时具有堆栈(FIFO)和队列(LIFO)操作行为
的数据结构。这个类和 Perl 语言中数组相像。需要实现四个方法：
shift() 返回并删除列表中的第一个元素，类似于前面的 dequeue()函数。
unshift() 在列表的头部"压入"一个新元素
push() 在列表的尾部加上一个新元素，类似于前面的 enqueue()和 push()方法。
pop() 返回并删除列表中的最后一个元素，与前面的 pop()方法完全一样。'''


class FourWaysControlList():

    def __init__(self, sq=[]):
        self.sq = [] + sq

    def shift(self):
        str = self.sq[0]
        self.sq.pop(0)
        return str

    def unshift(self, x):
        self.sq.insert(0, x)

    def push(self, x):
        self.sq.append(x)

    def pop(self):
        str = self.sq[-1]
        self.sq.pop()

    def __str__(self):
        return str(self.sq)


# 定义一个类，实现深度优先搜索和广度优先搜索两个方法
'''图的深度优先搜索(Depth First Search)，和树的先序遍历比较类似。

它的思想：假设初始状态是图中所有顶点均未被访问，则从某个顶点v出发，首先访问该顶点，然后依次从它的各个未被访问的邻接点出发深度优先搜索遍历图，直至图中所有和v有路径相通的顶点都被访问到。 若此时尚有其他顶点未被访问到，则另选一个未被访问的顶点作起始点，重复上述过程，直至图中所有顶点都被访问到为止。

显然，深度优先搜索是一个递归的过程。'''

'''广度优先搜索算法(Breadth First Search)，又称为"宽度优先搜索"或"横向优先搜索"，简称BFS。

它的思想是：从图中某顶点v出发，在访问了v之后依次访问v的各个未曾访问过的邻接点，然后分别从这些邻接点出发依次访问它们的邻接点，并使得“先被访问的顶点的邻接点先于后被访问的顶点的邻接点被访问，直至图中所有已被访问的顶点的邻接点都被访问到。如果此时图中尚有顶点未被访问，则需要另选一个未曾被访问过的顶点作为新的起始点，重复上述过程，直至图中所有顶点都被访问到为止。

换句话说，广度优先搜索遍历图的过程是以v为起点，由近至远，依次访问和v有路径相通且路径长度为1,2...的顶点。'''


class Graph(object):
    def __init__(self, *args, **kwargs):
        self.node_neighbors = {}
        self.visited = {}

    def add_nodes(self, nodelist):
        for node in nodelist:
            self.add_node(node)

    def add_node(self, node):
        if not node in self.nodes():
            self.node_neighbors[node] = []

    def add_edge(self, edge):
        u, v = edge
        if (v not in self.node_neighbors[u] and (u not in self.node_neighbors[v])):
            self.node_neighbors[u].append(v)
            if (u != v):
                self.node_neighbors[v].append(u)

    def nodes(self):
        return self.node_neighbors.keys()

    def depth_first_search(self, root=None):
        order = []

        def dfs(node):
            self.visited[node] = True
            order.append(node)
            for n in self.node_neighbors[node]:
                if not n in self.visited:
                    dfs(n)

        if root:
            dfs(root)
        for node in self.nodes():
            if not node in self.visited:
                dfs(node)
        print(order)
        return order

    def breadth_first_search(self, root=None):
        quene = []
        order = []

        def bfs():
            while len(quene) > 0:
                node = quene.pop(0)
                self.visited[node] = True
                for n in self.node_neighbors[node]:
                    if (not n in self.visited) and (not n in quene):
                        quene.append(n)
                        order.append(n)

        if root:
            quene.append(root)
            order.append(root)
        for node in self.nodes():
            if not node in self.visited:
                quene.append(node)
                order.append(node)
                bfs()
        print(order)
        return order


if __name__ == '__main__':
    g = Graph()
    g.add_nodes([i + 1 for i in range(8)])
    g.add_edge((1, 2))
    g.add_edge((1, 3))
    g.add_edge((2, 4))
    g.add_edge((2, 5))
    g.add_edge((4, 8))
    g.add_edge((5, 8))
    g.add_edge((3, 6))
    g.add_edge((3, 7))
    g.add_edge((6, 7))
    print("nodes:", g.nodes())
    order = g.breadth_first_search(1)
    order1 = g.depth_first_search(1)

