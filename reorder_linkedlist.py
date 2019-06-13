from LinkedList import Node, LinkedList


def locate_the_middle_node():
  cursor, ds_cursor = ll.head, ll.head
  while ds_cursor and ds_cursor.next_node:
    prev_cursor = cursor
    cursor = cursor.next_node
    ds_cursor = ds_cursor.next_node.next_node

  prev_cursor.next_node = None

  return cursor


def reverse_second_half(middle_node):
  cursor = middle_node
  next_cursor = cursor.next_node
  cursor.next_node = None
  prev_cursor = cursor
  cursor = next_cursor

  while cursor.next_node:
    next_cursor = cursor.next_node
    cursor.next_node = prev_cursor
    prev_cursor = cursor
    cursor = next_cursor

  cursor.next_node = prev_cursor

  return cursor


def reorder_ori_list(head_of_second_half):
  c1 = ll.head
  c2 = head_of_second_half
  while c1.next_node:
    tmp_node = c1.next_node
    c1.next_node = c2
    c1 = tmp_node
    tmp_node = c2.next_node
    c2.next_node = c1
    c2 = tmp_node
  c1.next_node = c2


# Main
ll = LinkedList()
ll.append(Node('A'))
ll.append(Node('B'))
ll.append(Node('C'))
ll.append(Node('D'))
ll.append(Node('E'))
ll.append(Node('F'))
ll.append(Node('G'))
ll.append(Node('H'))

middle_node = locate_the_middle_node()
head_of_second_half = reverse_second_half(middle_node)
reorder_ori_list(head_of_second_half)
ll.print_list()
