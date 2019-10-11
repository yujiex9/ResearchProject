from LinkedList import Node, LinkedList


def swap_lists(ll1, ll2):
  summing_list, summed_list = LinkedList(), LinkedList()
  if len(ll1) <= len(ll2):
    summing_list, summed_list = ll1, ll2
  else:
    summing_list, summed_list = ll2, ll1

  return summing_list, summed_list


def sum(ll1=LinkedList(), ll2=LinkedList()):
  result_list = LinkedList()
  summing_list, summed_list = swap_lists(ll1, ll2)

  carry = 0
  c1, c2 = summing_list.head, summed_list.head
  while c1 and c2:
    sum = c1.value + c2.value + carry
    if sum >= 10:
      sum -= 10
      carry = 1
    else:
      carry = 0
    result_list.append(Node(sum))
    c1 = c1.next_node
    c2 = c2.next_node

  while c2:
    sum = c2.value + carry
    if sum >= 10:
      sum -= 10
      carry = 1
    else:
      carry = 0
    result_list.append(Node(sum))
    if not c2.next_node and carry == 1:
      result_list.append(Node(carry))
    c2 = c2.next_node

  result_list.print_list()


ll1, ll2 = LinkedList(), LinkedList()
ll1.append(Node(3))
ll1.append(Node(4))
ll1.append(Node(5))
ll1.append(Node(6))
ll1.append(Node(7))
ll1.append(Node(8))
ll2.append(Node(9))
ll2.append(Node(8))
ll2.append(Node(7))
ll2.append(Node(6))
ll2.append(Node(5))

sum(ll1, ll2)
