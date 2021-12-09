class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


a = node(10)
b = node(20)
c = node(30)
d = node(40)
e = node(50)
f = node(60)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f



def mps(root)->int:
    if root == None:
        return 0

    if root.left == None or root.right == None:
        return root.data

    maxPathSum = max(mps(root.left),mps(root.right))
    print(maxPathSum)
    return root.data + maxPathSum


print(mps(a))


        #         10
        #     20      30
        # 40      50      60