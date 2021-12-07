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

# def includes(root,target):
#     if root == None:
#         return False

#     queue =[]

#     queue.append(root)
#     while(len(queue)>0):
#         current = queue.pop(0)
#         if current.data == target:
#             return True
        
#         if current.left:
#             queue.append(current.left)

#         if current.right:
#             queue.append(current.right)

#     return False

def includes(root,target):
    if root == None:
        return False

    if root.data == target:
        return True

    return includes(root.left,target) or includes(root.right,target)

#Time & Space Complexity O(n), where n is the No of nodes
print(includes(a,"e"))
#             a
#         /       \
#     b               c
# /     \             /
# d       e           f