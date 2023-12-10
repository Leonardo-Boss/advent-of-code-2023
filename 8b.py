import numpy
with open("inputs/8", "r") as f:
    data = f.readlines()

# with open("tests/8B", "r") as f:
#     data = f.readlines()

class Node:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right

def get_or_assign(name, nodes, left=None, right=None):
    n = nodes.get(name)
    if n:
        n.left = left if left else n.left
        n.right = right if right else n.right
        nodes[name] = n
        return n
    n = Node(name, left, right)
    nodes[name] = n
    return n

def read_graph(data, nodes):
    if len(data) == 0: return
    name, children = data[0].split(' = ')
    left, right = map(get_or_assign, children.removeprefix('(').removesuffix(')\n').split(', '),(nodes,nodes))
    get_or_assign(name, nodes, left, right)
    read_graph(data[1:], nodes)

def exec_ins(ins, node):
    for c in ins:
        if c == 'L':
            node = node.left
        else:
            node = node.right
    return node

def is_destiny(nodes):
    for node in nodes:
        if node.name[2] != 'Z':
            return False
    return True

ins = data[0].removesuffix('\n')

nodes = {}
read_graph(data[2:], nodes)

new_nodes = {}
ns = []
for node in nodes.values():
    next_node = exec_ins(ins, node)
    next_node = get_or_assign(next_node.name, new_nodes)
    node = get_or_assign(node.name, new_nodes, next_node)
    if node.name[2] == 'A':
        ns.append(node)

v = []
for i in ns:
    visited = []
    node = i.left
    counter = 0
    while node != i and node not in visited:
        visited.append(node)
        counter += 1
        node = node.left
    v.append(visited)

lens = [len(i) for i in v]
print(numpy.lcm.reduce(lens)*len(ins))
