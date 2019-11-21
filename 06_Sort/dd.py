
from random import seed
from random import randint
from math import log2
from math import floor
seed(1)


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, data=None):
        self.data = data

    def setNext(self, next=None):
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        if self.head is None:
            return "This List has no elements "
        else:
            cur_node = self.head
            str_ = ""
            while cur_node is not None:
                str_ = str_ + str(cur_node.getData()) + " "
                cur_node = cur_node.getNext()
            return str_

    def size(self):
        if self.head is None:
            return "This List has no element"
        else:
            cur_node = self.head
            count = 0
            while cur_node is not None:
                count += 1
                cur_node = cur_node.getNext()
            return count

    def append(self, data):
        append_node = None
        if not isinstance(data, Node):
            append_node = Node(data)
        else:
            append_node = data

        if self.head is None:
            self.head = append_node
            return
        cur_node = self.head
        while cur_node.getNext() is not None:
            cur_node = cur_node.getNext()
        cur_node.next = append_node

    def addHead(self, data):
        append_node = None
        if not isinstance(data, Node):
            append_node = Node(data)
        else:
            append_node = data

        append_node.setNext(self.head)
        self.head = append_node

    def nodeAt(self, i):
        p = self.head
        for _ in range(0, i):
            p = p.next
        return p

    def addAtIndex(self, index, data):
        append_node = None
        if not isinstance(data, Node):
            append_node = Node(data)
        else:
            append_node = data

        if index == 1:
            self.addHead(append_node)
            return
        else:
            cur_node = self.head
            cur_index = 1
            while cur_node is not None:
                if cur_index == index-1:
                    append_node.setNext(cur_node.getNext())
                    cur_node.setNext(append_node)
                cur_node = cur_node.getNext()
                cur_index += 1

    def isIn(self, data):
        if self.head is None:
            return False
        else:
            cur_node = self.head
            while cur_node is not None:
                if cur_node.getData() == data:
                    return True
                cur_node = cur_node.getNext()
            return False

    def before(self, data):
        if self.head is None or not self.isIn(data):
            return "This List has no elements"
        else:
            cur_node = self.head
            while cur_node.getNext() is not None:
                if cur_node.getNext().getData() == data:
                    break
                cur_node = cur_node.getNext()
            return cur_node

    def remove(self, data):
        if self.head is None or not self.isIn(data):
            return "This List has no element to delete"
        else:
            cur_node = self.head
            delete_node = None
            while cur_node.next is not None:
                if cur_node.getNext().getData() == data:
                    break
                cur_node = cur_node.getNext()
            if cur_node.getNext() is None:
                return "Item not found in the list"
            else:
                delete_node = cur_node.getNext()
                cur_node.setNext(delete_node.getNext())
                delete_node.setNext(None)
                return delete_node

    def removeTail(self):
        if self.head is None:
            return "The list has no element to delete"
        else:
            cur_node = self.head
            delete_node = None
            while cur_node.getNext().getNext() is not None:
                cur_node = cur_node.getNext()
            delete_node = cur_node.getNext()
            cur_node.setNext(None)
            return delete_node

    def removeHead(self):
        if self.head is None:
            return "This list has no element to delete"
        else:
            delete_node = None
            delete_node = self.head
            self.head = delete_node.getNext()
            delete_node.setNext(None)
            return delete_node

    def removeAtIndex(self, index):
        if index == 1:
            return self.removeHead()
        else:
            cur_node = self.head
            i = 1
            while cur_node is not None:
                if i == index:
                    return self.remove(cur_node.getData())
                cur_node = cur_node.getNext()
                i += 1


def random(lst, num):
    for _ in range(num):
        lst.append(randint(0, 99))


def print90(h, i, max_i):
    if i <= max_i:
        indent = floor(log2(i+1))
        print90(h, (i*2)+2, max_i)
        print('     ' * indent, h.nodeAt(i))
        print90(h, (i*2)+1, max_i)


def insertMinHeap(h, i):
    print('insert', h.nodeAt(i), 'at index ', i, end=' ')
    print(h)
    insertEle = h.nodeAt(i).getData()
    fi = (i-1)//2
    while i > 0 and insertEle < h.nodeAt(fi).getData():
        h.nodeAt(i).setData(h.nodeAt(fi).getData())
        i = fi
        fi = (i-1)//2
    h.nodeAt(i).setData(insertEle)


def deleteMin(h, last):
    print('delMin', h.nodeAt(0).getData(), 'last index = ', last, end='     ')
    print(h)
    insertEle = h.nodeAt(last).getData()
    h.nodeAt(last).setData(h.nodeAt(0).getData())
    hole = 0
    ls = hole*2 + 1
    found = False
    while ls < last and not found:
        rs = ls if ls+1 >= last else ls+1
        min = ls if h.nodeAt(ls).getData() < h.nodeAt(
            rs).getData() else rs  # minson index
        if h.nodeAt(min).getData() < insertEle:
            h.nodeAt(hole).setData(h.nodeAt(min).getData())
            hole = min  # going down the tree
            ls = hole*2+1
        else:
            found = True
    h.nodeAt(hole).setData(insertEle)


lst = []

random(lst, 10)
print(lst)

ll = LinkedList()
for i in lst:
    ll.append(i)
print90(ll, 0, ll.size()-1)

for i in range(0, ll.size()-1):
    insertMinHeap(ll, i)
    print(ll)
    print90(ll, 0, i)
    print("----------------------------------\n")

temp = []
for last in range(ll.size()-2, -1, -1):
    temp.append(ll.nodeAt(0).getData())
    deleteMin(ll, last)
    print(ll)
    print90(ll, 0, last-1)
    print('------------------\n')

