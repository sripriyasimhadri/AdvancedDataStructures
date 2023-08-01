#MinHeap Implementation
class ImplementHeap_Min:
    #Constructor
    def __init__(self):
        self.min_hp_lst = [0]
        self.siz_min_heap = 0

    #Min Heap insert helper
    def min_heap_ins(self, ele):
        self.min_hp_lst.append(ele)
        self.siz_min_heap += 1
        self.up_heap_min(self.siz_min_heap)

    #Method to perform heapify operation
    def up_heap_min(self, s):
        while (s // 2) > 0:
            if self.min_hp_lst[s].ride.less_than(self.min_hp_lst[s // 2].ride):
                self.exchange(s, (s // 2))
            else:
                break
            s = s // 2

        # Method to pop element from minHeap
        def mHeapPopMethod(self):
            if len(self.min_hp_lst) == 1:
                return 'No Rides Available'
            rt_node = self.min_hp_lst[1]
            self.exchange(1, self.siz_min_heap)
            self.siz_min_heap -= 1
            *self.min_hp_lst, _ = self.min_hp_lst
            self.mHeap_low(1)
            return rt_node

    #Min heap low function
    def mHeap_low(self, s):
        while (s * 2) <= self.siz_min_heap:
            dex = self.get_min_child_index(s)
            if not self.min_hp_lst[s].ride.less_than(self.min_hp_lst[dex].ride):
                self.exchange(s, dex)
            s = dex

        # Method to pop element from minHeap
    def mHeapPopMethod(self):
        if len(self.min_hp_lst) == 1:
                return 'No Rides Available'
            rt_node = self.min_hp_lst[1]
            self.exchange(1, self.siz_min_heap)
            self.siz_min_heap -= 1
            *self.min_hp_lst, _ = self.min_hp_lst
            self.mHeap_low(1)
            return rt_node
    #Method to get smallest element in the minHeap
    def get_min_child_index(self, s):
        if (s * 2) + 1 > self.siz_min_heap:
            return s * 2
        else:
            if self.min_hp_lst[s * 2].ride.less_than(self.min_hp_lst[(s * 2) + 1].ride):
                return s * 2
            else:
                return (s * 2) + 1

    #Method to change element to new
    def ele_change_new(self, s, nke):
        point = self.min_hp_lst[s]
        point.ride.trip_duration = nke
        if s == 1:
            self.mHeap_low(s)
        elif self.min_hp_lst[s // 2].ride.less_than(self.min_hp_lst[s].ride):
            self.mHeap_low(s)
        else:
            self.up_heap_min(s)

    #Method to remove element from minHeap
    def remove_mHeap(self, p):
        self.exchange(p, self.siz_min_heap)
        self.siz_min_heap -= 1
        *self.min_hp_lst, _ = self.min_hp_lst
        self.mHeap_low(p)

