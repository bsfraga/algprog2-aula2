from node_core import Node


class List:

    def __init__(self, head=None):
        """ Constructor method from List. This method initialize the list."""

        self.head = head

    def insert(self, data):
        """
        This method insert new data into the current list.
        """

        new_node = Node(data=data)
        new_node.set_next(self.head)
        self.head = new_node

    def get_items(self):
        """
        This method iterate over the list and print the data inside of it.
        """

        current = self.head
        print('\nPrinting data inside the list....')

        while current:
            print(f'{current.get_data()}, ')
            current = current.get_next()

    def size(self):
        """
        This method returns the total size from the current list.
        """

        current = self.head
        counter = 0

        while current:
            counter += 1
            current = current.get_next()

        return counter

    def search(self, data):
        """
        This method perform a search inside the current list for a specific value.
        #Returns:
           current: The value searched if present on current list.

        #Exception:           
           ValueError Exception: If the value is not present in the current list.  
        """

        current = self.head
        found = False
        print(f'Searching for: "{data}" ....')

        while current and found is False:

            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()

        if current is None:
            raise ValueError("Informed value not present in current list.")

        return current.get_data()

    def delete(self, data):
        """
        This method remove a value from the current list.

        #Exception:
            ValueError Exception: If the value is not present in the current list. 
        """

        current = self.head
        previous = None
        found = False

        print(f'Removing value : "{data}" ....')

        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()

        if current is None:
            raise ValueError("Informed value not present in current list.")

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
