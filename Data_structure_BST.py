class BNode:
    def __init__(self, x):
        self.data = x
        self.Lchild = None
        self.Rchild = None

class BST:
    def __init__(self):
        self.root = None
        self.list = []

    def add(self, x):
        if self.root is None:
            self.root = BNode(x)
            self.list.append(x)
        else:
            self.padd(self.root, x)

    def padd(self, root, x):
        if x > root.data:
            if root.Rchild is None:
                root.Rchild = BNode(x)
                self.list.append(x)
            else:
                self.padd(root.Rchild, x)
        elif x < root.data:
            if root.Lchild is None:
                root.Lchild = BNode(x)
                self.list.append(x)
            else:
                self.padd(root.Lchild, x)

    def show(self):
        return self.pshow(self.root)

    def pshow(self, root):
        if root:
            self.pshow(root.Lchild)
            print(root.data, end=" ")
            self.pshow(root.Rchild)

def createList(Tree):
    print(Tree.list)

def createTree(A):
    Tree = BST()
    for i in A:
        Tree.add(i)
    return Tree

if __name__ == "__main__":
    data = [10, 5, 15, 3, 7, 12, 18]
    tree = createTree(data)
    print("BST elements in order:")
    tree.show()
    print()
    createList(tree)
