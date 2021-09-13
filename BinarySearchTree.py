class Node:
    def __init__(self, key):
        self.key = key
        self.parent, self.left, self.right = None, None, None

    def __int__(self):
        return self.key


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def find_location(self, key):
        if self.size == 0:
            return None
        p = None
        v = self.root
        while v != None:
            if key == v.key:
                return v
            elif v.key < key:
                p = v
                v = v.right
            else:
                p = v
                v = v.left
        return p

    def search(self, key):
        v = self.find_location(key)
        if v == None or v.key != key:
            return None
        else:
            return v

    def insert(self, key):
        p = self.find_location(key)
        if p == None or p.key != key:
            v = Node(key)
            if p == None:
                self.root = v
            else:
                if p.key > key:
                    p.left = v
                else:
                    p.right = v
            self.size += 1
            v.parent = p
            return v
        else:
            print("key is already insert")
            return

    def merge_delete(self, X):
        a = X.left
        b = X.right
        p = X.parent

        if a != None:
            c = a
            m = a
            while m.right != None:
                m = m.right
                if b != None:
                    b.parent = m
                    m.right = b
        else:
            c = b

        if p != None:
            if c:
                c.parent = p
            if c.key < p.key:
                p.left = c
            else:
                p.right = c
        else:
            self.root = c
            if c:
                c.parent = None
        self.size -= 1

    def copy_delete(self, X):
        a = X.left
        b = X.right
        p = X.parent

        if a != None:
            m = a
            while m.right != None:
                m = m.right
            if m.left != None:
                m.left.parent = m.parent
                m.parent.right = m.left

            c = m
            c.left = a
            c.right = b
            a.parent = c
            b.parent = c

        print("return??")
        if p != None:
            if c:
                c.parent = p
            if c.key < p.key:
                p.left = c
            else:
                p.right = c
        else:
            self.root = c
            c.parent = None
        self.size -= 1


X = BST()

X.insert(15)
X.insert(4)
X.insert(20)
X.insert(2)
X.insert(17)
X.insert(32)
X.insert(16)
X.insert(18)
X.insert(19)
X.insert(39)
