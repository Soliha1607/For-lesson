class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, key):
        current = self.head

        if current and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next
        current = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=", ")
            current = current.next
        print("None")


students = LinkedList()
subjects = LinkedList()
teachers = LinkedList()

students.append("Someone")
students.append("Someone1")
students.append("Someone2")
students.append("Someone3")

subjects.append("Math")
subjects.append("Physics")
subjects.append("English")

teachers.append("Somebody")
teachers.append("Somebody1")
teachers.append("Somebody2")

students.delete("Someone1")
subjects.delete("Physics")
teachers.delete("Somebody")

print("Students:")
students.display()

print("\nSubjects:")
subjects.display()

print("\nTeachers:")
teachers.display()
