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


def totalSum(root):
    if root == None:
        return 0
  
    return root.data + totalSum(root.left) + totalSum(root.right)
    
#Time & Space Complexity O(n), where n is the No of nodes
print(totalSum(a))
#             a
#         /       \
#     b               c
# /     \             /
# d       e           f