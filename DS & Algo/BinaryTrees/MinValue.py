class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


a = node(50)
b = node(20)
c = node(30)
d = node(40)
e = node(10)
f = node(60)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f

def minValue(root):
    if root == None:
        return float("inf")

    lval =minValue(root.left)

    rval =minValue(root.right)

    return min(root.data, lval, rval)



print(minValue(a))