def solution():
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    class LinkedList:
        def __init__(self):
            self.head = None

        def insert_end(self, data):
            new_node = Node(data)

            if self.head is None:
                self.head = new_node
                return

            temp = self.head
            while temp.next:
                temp = temp.next

            temp.next = new_node

        def display(self):
            temp = self.head
            values = []

            while temp:
                values.append(str(temp.data))
                temp = temp.next

            print(" ".join(values))

        def insert_position(self, data, pos):
            new_node = Node(data)

            if pos == 1:
                new_node.next = self.head
                self.head = new_node
                return

            temp = self.head

            for _ in range(pos - 2):
                if temp is None:
                    return
                temp = temp.next

            if temp is None:
                return

            new_node.next = temp.next
            temp.next = new_node

        def middle(self):
            slow = self.head
            fast = self.head

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            if slow:
                print(slow.data)

        def delete(self, value):
            temp = self.head

            if temp and temp.data == value:
                self.head = temp.next
                return

            while temp and temp.next:
                if temp.next.data == value:
                    temp.next = temp.next.next
                    return

                temp = temp.next

        def reverse(self):
            prev = None
            curr = self.head

            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            self.head = prev

        def consecutive_sum(self):
            temp = self.head

            while temp and temp.next:
                print(temp.data + temp.next.data)
                temp = temp.next

    ll = LinkedList()

    n = int(input())
    values = list(map(int, input().split()))

    for value in values[:n]:
        ll.insert_end(value)

    ll.display()

    pos = int(input())
    data = int(input())

    ll.insert_position(data, pos)
    ll.display()

    ll.middle()

    value = int(input())
    ll.delete(value)
    ll.display()

    ll.reverse()
    ll.display()

    ll.consecutive_sum()


if __name__ == "__main__":
    solution()