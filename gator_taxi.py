import sys
from ImplementHeap_Min import ImplementHeap_Min
from NodeOfMinHeap import NodeOfMinHeap
from ImplementReBlTree import ImplementReBlTree
from NodeOfRedBlackTree import NodeOfRedBlackTree

#Class for a ride structure as defined in the question
class ClassRTemplate:
    #Constructor for class
    def __init__(self, ride_num, ride_cost, trip_duration):
        self.ride_num = ride_num
        self.ride_cost = ride_cost
        self.trip_duration = trip_duration
    #Finding out cheaper ride
    def less_than(self, ride_other):
        if self.ride_cost < ride_other.ride_cost:
            return True
        elif self.ride_cost > ride_other.ride_cost:
            return False
        elif self.ride_cost == ride_other.ride_cost:
            if self.trip_duration > ride_other.trip_duration:
                return False
            else:
                return True


#A method to write output to the destined output file
def writeToOutputFile(ride, txt, lst):
    fl = open("output_file.txt", "a")
    if ride is None:
        fl.write(txt + "\n")
    else:
        txt = ""
        if not lst:
            txt += ("(" + str(ride.ride_num) + "," + str(ride.ride_cost) + "," + str(ride.trip_duration) + ")\n")
        else:
            if len(ride) == 0:
                txt += "(0,0,0)\n"
            for i in range(len(ride)):
                if i != len(ride) - 1:
                    txt = txt + ("(" + str(ride[i].ride_num) + "," + str(ride[i].ride_cost) + "," + str(
                        ride[i].trip_duration) + "),")
                else:
                    txt = txt + ("(" + str(ride[i].ride_num) + "," + str(ride[i].ride_cost) + "," + str(
                        ride[i].trip_duration) + ")\n")

        fl.write(txt)
    fl.close()


#A method to insert a ride and check if it a duplicate
def insertARide(rd, hp, redBlackTree):
    if redBlackTree.ride_finder(rd.ride_num) is not None:
        writeToOutputFile(None, "Duplicate RideNumber", False)
        sys.exit(0)
        return
    rbt_node = NodeOfRedBlackTree(None, None)
    min_heap_node = NodeOfMinHeap(rd, rbt_node, hp.siz_min_heap + 1)
    hp.min_heap_ins(min_heap_node)
    redBlackTree.insertRBTMethod(rd, min_heap_node)

#method to print the ride
def ridePrint(numberOfRide, redBlackTree):
    op = redBlackTree.ride_finder(numberOfRide)
    if op is None:
        writeToOutputFile(ClassRTemplate(0, 0, 0), "", False)
    else:
        writeToOutputFile(op.ride, "", False)

def ridesPrinter(f, g, redBlackTree):
    list = redBlackTree.findRideRange(f, g)
    writeToOutputFile(list, "", True)

#A method to get the next ride
def nextRideGet(hp, redBlackTree):
    if hp.siz_min_heap != 0:
        popped_node = hp.mHeapPopMethod()
        redBlackTree.nodeDelete(popped_node.ride.ride_num)
        writeToOutputFile(popped_node.ride, "", False)
    else:
        writeToOutputFile(None, "No active ride requests", False)

#A method to cancel the ride
def rideCancelHelper(numberOfRide, hp, redBlackTree):
    nodeHeap = redBlackTree.nodeDelete(numberOfRide)
    if nodeHeap is not None:
        hp.remove_mHeap(nodeHeap.min_heap_index)

#A method to update the current ride
def rideUpdate(numberOfRide, updatedDuration, hp, redBlackTree):
    nodeRBT = redBlackTree.ride_finder(numberOfRide)
    if nodeRBT is None:
        print("")
    elif updatedDuration <= nodeRBT.ride.trip_duration:
        hp.ele_change_new(nodeRBT.min_heap_node.min_heap_index, updatedDuration)
    elif nodeRBT.ride.trip_duration < updatedDuration <= (2 * nodeRBT.ride.trip_duration):
        rideCancelHelper(nodeRBT.ride.ride_num, hp, redBlackTree)
        insertARide(ClassRTemplate(nodeRBT.ride.ride_num, nodeRBT.ride.ride_cost + 10, updatedDuration), hp, redBlackTree)
    else:
        rideCancelHelper(nodeRBT.ride.ride_num, hp, redBlackTree)

#MAIN
if __name__ == "__main__":
    #MinHeap Object
    hp = ImplementHeap_Min()
    #RedBlackTree Object
    redBlackTree = ImplementReBlTree()
    #Writer
    fl = open("output_file.txt", "w")
    fl.close()
    #Reader
    fl = open(sys.argv[1], "r")
    for h in fl.readlines():
        k = []
        for g in h[h.index("(") + 1:h.index(")")].split(","):
            if g != '':
                k.append(int(g))
        #Insert method call
        if "Insert" in h:
            insertARide(ClassRTemplate(k[0], k[1], k[2]), hp, redBlackTree)
        #Print method call
        elif "Print" in h:
            if len(k) == 1:
                ridePrint(k[0], redBlackTree)
            elif len(k) == 2:
                ridesPrinter(k[0], k[1], redBlackTree)
        #Update ride method call
        elif "UpdateTrip" in h:
            rideUpdate(k[0], k[1], hp, redBlackTree)
        #Get next ride method call
        elif "GetNextRide" in h:
            nextRideGet(hp, redBlackTree)
        #Cancel ride method call
        elif "CancelRide" in h:
            rideCancelHelper(k[0], hp, redBlackTree)