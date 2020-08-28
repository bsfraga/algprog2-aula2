class Node:

    def __init__(self, data=None, next_node=None):
        """
        Constructor method from List. This method initialize the Node.
        """

        self.data = data
        self.next_node = next_node

    def get_data(self):
        """
        This method returns the data inside the current Node.
        """

        return self.data

    def get_next(self):
        """
        This method returns the next instance of Node.
        """

        return self.next_node

    def set_next(self, new_next):
        """
        This method initialize the next node with the informed parameters.

        #Parameters:
            new_next: Data for the new next Node.
        """
        
        self.next_node = new_next
