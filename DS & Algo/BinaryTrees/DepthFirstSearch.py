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

# def depthFirstSearch(root)->list:
#     if root ==None:
#         return []

#     stack,result = [],[]
#     stack.append(root)

#     while len(stack) > 0:
#         current = stack.pop()
#         result.append(current.data)
#         if current.right:
#             stack.append(current.right)
#         if current.left:
#             stack.append(current.left)

#     return result

#Time & Space Complexity O(n), where n is the No of nodes.
def depthFirstSearch(root,arr =[]):
    if root == None:
        return []
    arr.append(root.data)
    if root.left:
        depthFirstSearch(root.left,arr)
    if root.right:
        depthFirstSearch(root.right,arr)

    return arr
    


print(depthFirstSearch(a))
