#Class to define node structure in red black tree
class NodeOfRedBlackTree:
    def __init__(self, rdID, node_of_min_heap):
        self.ride = rdID
        self.parent = None  # parent node
        self.left = None  # left node
        self.right = None  # right node
        self.color = 1  # 1=red , 0 = black
        self.min_heap_node = node_of_min_heap