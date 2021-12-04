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

#Time & Space Complexity O(n), where n is the No of nodes.
def bfs(root)->list:
    if root == None:
        return []

    queue,result =[],[]
    queue.append(root)

    while (len(queue)>0):

        current = queue.pop(0)
        result.append(current.data)

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    return result


    
print(bfs(a))

