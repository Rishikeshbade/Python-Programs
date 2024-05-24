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
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def search(self, key):
        current = self.head
        prev = None
        while current:
            if current.data == key:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True  # Found and removed
            prev = current
            current = current.next
        return False  # Not found

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            current = self.head
            while current:
                file.write(current.data + '\n')
                current = current.next


def main():
    filename = 'word_list.txt'
    words = LinkedList()

    # Read words from file and build linked list
    with open(filename, 'r') as file:
        for word in file:
            word = word.strip()
            if word:
                words.append(word)

    # User input to search/add/remove words
    while True:
        print("\nCurrent word list:")
        words.display()
        choice = input("Enter a word to search/add/remove (type 'quit' to exit): ").strip()
        if choice == 'quit':
            break
        if words.search(choice):
            print(f"'{choice}' removed from the list.")
        else:
            words.append(choice)
            print(f"'{choice}' added to the list.")

    # Save updated list to file
    words.save_to_file(filename)
    print("Word list saved to", filename)


