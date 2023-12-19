# NOTE: Graded 100/100
# NOTE: All tests pass

from types import SimpleNamespace
import sys

class LinkedList(object):
    def __init__(self):
        self.__first = None
        self.__last = None
        self.__length = 0

    def append(self, value):
        if not self:
            self.__first = self.__makenode(value)
            self.__last = self.__first

        else:
            new_last = self.__makenode(value, self.__last)
            self.__last.next = new_last
            self.__last = new_last

        self.__length += 1

    def pop(self, i=-1):
        i = self.__getindex(i)
        node = self.__getnode(i)

        if i == 0:
            self.__first = self.__first.next

        elif i == len(self) - 1:
            self.__last = self.__last.prev
            self.__last.next = None

        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        self.__length -= 1

    def swap(self, ix, iy):
        self[ix], self[iy] = self[iy], self[ix]

    def __makenode(self, value, prev=None, next=None):
        return SimpleNamespace(value=value, prev=prev, next=next)

    def __getnode(self, i):
        i = self.__getindex(i)
        curr_node = self.__first

        if i == 0:
            return curr_node

        for j in range(i):
            curr_node = curr_node.next

        return curr_node

    def __getindex(self, i):
        if i < 0:
            i = len(self) + i

        if i < 0 or i >= len(self):
            raise IndexError("list index out of range")

        return i

    def __getitem__(self, i):
        return self.__getnode(i).value

    def __setitem__(self, i, item):
        self.__getnode(i).value = item

    def __delitem__(self, i):
        self.pop(i)

    def __iter__(self):
        curr_node = self.__first
        if not curr_node:
            return

        yield curr_node.value
        while curr_node := curr_node.next:
            yield curr_node.value

    def __len__(self):
        return self.__length

    def __bool__(self):
        return bool(len(self))

    def __repr__(self):
        return f"LinkedList({list(self)!r})"

    def __str__(self):
        return str(list(self))


train_list = LinkedList()

def tr_push(train_id, weight):
    try:
        train_list.append((train_id, int(weight)))
        print("ok")

    except ValueError:
        print("error")

def tr_pop_pos(train_pos):
    try:
        del train_list[int(train_pos)]
        print("ok")

    except (ValueError, IndexError):
        print("error")

def tr_pop_id(train_id):
    match = list(filter(lambda it: it[1] == train_id, map(lambda n:
        (n[0], n[1][0],), enumerate(train_list))))

    if not match:
        print("error")
        return

    del train_list[match[0][0]]
    print("ok")

def tr_move(train_id, pos):
    match = list(filter(lambda it: it[1] == train_id, map(lambda n:
        (n[0], n[1][0],), enumerate(train_list))))

    if not match:
        print("error")
        return

    try:
        from_pos = match[0][0]
        train_list.swap(from_pos, int(pos)-1)
        print("ok")

    except ValueError:
        print("error")

def tr_total_weight():
    print(sum(map(lambda it: it[1], train_list)))

def tr_print():
    if not train_list:
        print("empty")

    else:
        print("\n".join(map(lambda it: f"{it[0]}:{it[1]}", train_list)))


for line in sys.stdin:
    line = line.strip()
    if line.startswith("push"):
        tr_push(*line.split(" ")[1:])
    elif line.startswith("pop id:"):
        tr_pop_id(line[7:])
    elif line.startswith("pop pos:"):
        tr_pop_pos(line[8:])
    elif line.startswith("move"):
        tr_move(*line.split(" ")[1:])
    elif line.startswith("total_weight"):
        tr_total_weight()
    elif line.startswith("print"):
        tr_print()
    else:
        print("error")