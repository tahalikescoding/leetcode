
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self,val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next 
            cur.next = new_node

    def traverse(self):
        if self.head is None:
            raise IndexError("Singly linked List is empty")

        else:
            cur = self.head
            while cur is not None:
                print(cur.val , end = " ")
                cur = cur.next

    def insert(self,val,pos):
        new_node = Node(val)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            cur = self.head
            prev = None
            count = 0 
            while cur is not None and count<pos:
                prev = cur
                cur = cur.next 
                count +=1 
            prev.next = new_node
            new_node.next = cur

    def delete(self,val):
        temp = self.head
        if temp is not None:
            if temp.val == val:
                self.head = temp.next
                del temp
                return
            else:
                prev = None
                found = False
                while temp is not None:
                    if temp.val == val:
                        found = True
                        break
                    prev = temp
                    temp = temp.next
                if found:
                    prev.next = temp.next
                    del temp
                    return
                else:
                    raise IndexError(f"{val} Not found")

if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.append(7)
    sll.append(80)
    sll.append(900)
    sll.append(763)
    sll.traverse()
    sll.insert(67,3)
    sll.traverse()
    sll.delete(67)
    sll.traverse()
            