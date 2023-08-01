#Class to define node structure in min Heap
class NodeOfMinHeap:
    def __init__(self, rdID, rebt, inde_of_min_heap):
        self.ride = rdID
        self.rbTree = rebt
        self.min_heap_index = inde_of_min_heap