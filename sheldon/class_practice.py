# 有一个data数据域，left，right 两个指针域
class TreeNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


class BTree:
    def __init__(self, root=0):
        self.root = root


class search:

    def depth_first(self, B_tree):
        node = B_tree
        print(node.data)
        if isinstance(node.left, TreeNode):
            self.depth_first(node.left)
        else:
            print(node.left)
        if isinstance(node.right, TreeNode):
            self.depth_first(node.right)
        print(node.right)
        # return


if __name__ == '__main__':
    node1_1 = TreeNode(2, 2.1, 2.2)
    node1 = TreeNode(1, node1_1, 3)
    node2 = TreeNode(4, 5, 6)
    node3 = TreeNode(0, node1, node2)
    Tree_root = BTree(node3)
    print(Tree_root.root)
    print(dir(Tree_root))

    search_ojb = search()
    search_ojb.depth_first(Tree_root.root)
