class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Hashmap to store key-node pairs
        self.head = Node(0, 0)  # Dummy head of the doubly linked list
        self.tail = Node(0, 0)  # Dummy tail of the doubly linked list
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        """Helper function to remove a node from the doubly linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_front(self, node: Node):
        """Helper function to add a node to the front of the doubly linked list."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)  # Remove the node from its current position
            self._add_to_front(node)  # Move it to the front (most recently used)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update the node's value and move it to the front
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_front(node)
        else:
            # If capacity is reached, remove the least recently used node
            if len(self.cache) == self.capacity:
                lru_node = self.tail.prev  # Least recently used node
                self._remove(lru_node)
                del self.cache[lru_node.key]
            # Add the new node to the front and update the hashmap
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)