class node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

root = node(10)
root.left = node(3)
root.right = node(5)
root.left.right = node(4)
root.left.left = node(8)
root.right.left = node(6)
root.right.right = node(7)
root.left.left.left = node(0)

def display(root):
    if root is None:
        return
    print(root.data,end=" ")
    display(root.left)
    display(root.right)

display(root)
print()
def pro(root):
    total_pro = 1
    if root is None:
        return 1
    total_pro = root.data* pro(root.left) * pro(root.right) 
    return total_pro
# y = pro(root)
# print(y)
print()
def sum_Nodes(root):
    sum = 0
    if root is None:
        return 0
    sum = root.data + sum_Nodes(root.left) + sum_Nodes(root.right)
    return sum
# x = sum_Nodes(root)
# print(x)
print()

def sum_nonzero(root):
    sum = 0
    if root is None:
        return 0
    if root.data==0:
        pass
    sum = root.data + sum_nonzero(root.left) + sum_nonzero(root.right)
    return sum
# z = sum_nonzero(root)
# print(z)
print()

def maximum(root):
    if root is None:
        return float('-inf')
    return max(root.data,maximum(root.left),maximum(root.right))
# a = maximum(root)
# print(a)
print()
def minimum(root):
    if root is None:
        return float('inf')
    return min(root.data,minimum(root.left),minimum(root.right))
# b = minimum(root)
# print(b)
print()

def levels(root):
    if root is None:
        return 0
    return 1 + max(levels(root.left),levels(root.right))
# c = levels(root)
# print(c)

# mirror tree
def mirror(root):
    if root is None:
        return 
    temp = root.right
    root.right = root.left
    root.left = temp
    mirror(root.left)
    mirror(root.right)

mirror(root)
print()
display(root)