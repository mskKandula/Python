class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


a = node('a')
b = node('b')
c = node('c')
d = node('d')
e = node('e')
f = node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f

#             a
#         /       \
#     b               c
# /     \             /
# d       e           f