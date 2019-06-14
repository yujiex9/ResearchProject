from LinkedList import Node, LinkedList


def swap_neighbours():
  if not ll.head or not ll.head.next_node:
    return

  cs = ll.head
  ncs = cs.next_node
  cs.next_node = ncs.next_node
  ncs.next_node = cs
  ll.head = ncs
  pcs = cs
  cs = cs.next_node

  while cs and cs.next_node:
    ncs = cs.next_node
    cs.next_node = ncs.next_node
    ncs.next_node = cs
    pcs.next_node = ncs
    pcs = cs
    cs = cs.next_node


# Main
ll = LinkedList()
for _node in [Node('A'), Node('B'), Node('C'), Node('D'), Node('E'), Node('F'), Node('G')]:
  ll.append(_node)

swap_neighbours()
ll.print_list()
