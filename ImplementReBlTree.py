from NodeOfRedBlackTree import NodeOfRedBlackTree

#Red Black Tree Data Structure Implementor
class ImplementReBlTree:
    def __init__(self):
        self.blankNode = NodeOfRedBlackTree(None, None)
        self.blankNode.left = None
        self.blankNode.right = None
        self.blankNode.color = 0
        self.root = self.blankNode

    # Method to check and find ride with the number equal to the ky provided in the arguments
    def ride_finder(self, ky):
        tmp = self.root
        # Iterate to find the ky
        while tmp != self.blankNode:
            if tmp.ride.ride_num == ky:
                return tmp
            if tmp.ride.ride_num < ky:
                tmp = tmp.right
            else:
                tmp = tmp.left
        return None

    # Method to balance the red black tree after a deletion
    def treeBalanceAfDel(self, den):
        while den != self.root and den.color == 0:
            if den == den.parent.right:
                parent_sibling = den.parent.left
                if parent_sibling.color != 0:
                    den.parent.color = 1
                    parent_sibling.color = 0
                    self.rightRotateRB(den.parent)
                    parent_sibling = den.parent.left

                if parent_sibling.right.color == 0 and parent_sibling.left.color == 0:
                    parent_sibling.color = 1
                    den = den.parent
                else:
                    if parent_sibling.left.color != 1:
                        parent_sibling.right.color = 0
                        parent_sibling.color = 1
                        self.leftRotateRB(parent_sibling)
                        parent_sibling = den.parent.left

                    parent_sibling.color = den.parent.color
                    den.parent.color = 0
                    parent_sibling.left.color = 0
                    self.rightRotateRB(den.parent)
                    den = self.root
            else:
                parent_sibling = den.parent.right
                if parent_sibling.color != 0:
                    den.parent.color = 1
                    parent_sibling.color = 0
                    self.leftRotateRB(den.parent)
                    parent_sibling = den.parent.right

                if parent_sibling.right.color == 0 and parent_sibling.left.color == 0:
                    parent_sibling.color = 1
                    den = den.parent
                else:
                    if parent_sibling.right.color != 1:
                        parent_sibling.left.color = 0
                        parent_sibling.color = 1
                        self.rightRotateRB(parent_sibling)
                        parent_sibling = den.parent.right

                    parent_sibling.color = den.parent.color
                    den.parent.color = 0
                    parent_sibling.right.color = 0
                    self.leftRotateRB(den.parent)
                    den = self.root
        den.color = 0

    #Method to tranplant nodes in a red black tree
    def transplantRBT(self, node, child_node):
        if node.parent is None:
            self.root = child_node
        elif node == node.parent.right:
            node.parent.right = child_node
        else:
            node.parent.left = child_node
        child_node.parent = node.parent


    #Method to delete a node
    def helDelNode(self, den, ky):
        delNode = self.blankNode
        while den != self.blankNode:
            if den.ride.ride_num == ky:
                delNode = den
            if den.ride.ride_num >= ky:
                den = den.left
            else:
                den = den.right

        if delNode == self.blankNode:
            return
        hNode = delNode.min_heap_node
        tm = delNode
        oriColY = tm.color
        if delNode.left == self.blankNode:
            tm1 = delNode.right
            self.transplantRBT(delNode, delNode.right)
        elif (delNode.right == self.blankNode):
            tm1 = delNode.left
            self.transplantRBT(delNode, delNode.left)
        else:
            tm = self.findMin(delNode.right)
            oriColY = tm.color
            tm1 = tm.right
            if tm.parent == delNode:
                tm1.parent = tm
            else:
                self.transplantRBT(tm, tm.right)
                tm.right = delNode.right
                tm.right.parent = tm

            self.transplantRBT(delNode, tm)
            tm.left = delNode.left
            tm.left.parent = tm
            tm.color = delNode.color
        if oriColY == 0:
            self.treeBalanceAfDel(tm1)
        return hNode

    #Method to balance red black tree after insert
    def balInsert(self, nodCurrent):
        while nodCurrent.parent.color == 1:
            if nodCurrent.parent == nodCurrent.parent.parent.left:
                parentSibVar = nodCurrent.parent.parent.right

                if parentSibVar.color == 0:
                    if nodCurrent == nodCurrent.parent.right:
                        nodCurrent = nodCurrent.parent
                        self.leftRotateRB(nodCurrent)
                    nodCurrent.parent.color = 0
                    nodCurrent.parent.parent.color = 1
                    self.rightRotateRB(nodCurrent.parent.parent)
                else:
                    parentSibVar.color = 0
                    nodCurrent.parent.color = 0
                    nodCurrent.parent.parent.color = 1
                    nodCurrent = nodCurrent.parent.parent

            else:
                parentSibVar = nodCurrent.parent.parent.left
                if parentSibVar.color == 0:
                    if nodCurrent == nodCurrent.parent.left:
                        nodCurrent = nodCurrent.parent
                        self.rightRotateRB(nodCurrent)
                    nodCurrent.parent.color = 0
                    nodCurrent.parent.parent.color = 1
                    self.leftRotateRB(nodCurrent.parent.parent)
                else:
                    parentSibVar.color = 0
                    nodCurrent.parent.color = 0
                    nodCurrent.parent.parent.color = 1
                    nodCurrent = nodCurrent.parent.parent

            if nodCurrent == self.root:
                break
        self.root.color = 0

    #Method to find a ride in given price range
    def lookForRideInPriceRange(self, nd, small, big, op):
        if nd == self.blankNode:
            return

        if small < nd.ride.ride_num:
            self.lookForRideInPriceRange(nd.left, small, big, op)
        if small <= nd.ride.ride_num <= big:
            op.append(nd.ride)
        self.lookForRideInPriceRange(nd.right, small, big, op)

    #Method to find ride in a given price range
    def findRideRange(self, small, big):
        op = []
        self.lookForRideInPriceRange(self.root, small, big, op)
        return op

    #Method to find smallest node
    def findMin(self, nd):
        while nd.left != self.blankNode:
            nd = nd.left
        return nd

    #Method to rotate the Red Black tree in left direction
    def leftRotateRB(self, s):
        t = s.right
        s.right = t.left
        if t.left != self.blankNode:
            t.left.parent = s

        t.parent = s.parent
        if s.parent == None:
            self.root = t
        elif s == s.parent.left:
            s.parent.left = t
        else:
            s.parent.right = t
        t.left = s
        s.parent = t

    # Method to rotate the Red Black tree in right direction
    def rightRotateRB(self, s):
        t = s.left
        s.left = t.right
        if t.right != self.blankNode:
            t.right.parent = s

        t.parent = s.parent
        if s.parent == None:
            self.root = t
        elif s == s.parent.right:
            s.parent.right = t
        else:
            s.parent.left = t
        t.right = s
        s.parent = t


    #Method to insert a new node into a red black tree
    def insertRBTMethod(self, rd, minHeap):
        nd = NodeOfRedBlackTree(rd, minHeap)
        nd.parent = None
        nd.left = self.blankNode
        nd.right = self.blankNode
        nd.color = 1

        nodeInsertor = None
        nodeTemporary = self.root

        while nodeTemporary != self.blankNode:
            nodeInsertor = nodeTemporary
            if nd.ride.ride_num < nodeTemporary.ride.ride_num:
                nodeTemporary = nodeTemporary.left
            else:
                nodeTemporary = nodeTemporary.right

        nd.parent = nodeInsertor
        if nodeInsertor is None:
            self.root = nd
        elif nd.ride.ride_num > nodeInsertor.ride.ride_num:
            nodeInsertor.right = nd
        else:
            nodeInsertor.left = nd

        if nd.parent is None:
            nd.color = 0
            return

        if nd.parent.parent is None:
            return

        self.balInsert(nd)

    #Method to delete a node in red black tree
    def nodeDelete(self, numberOfRide):
        return self.helDelNode(self.root, numberOfRide)