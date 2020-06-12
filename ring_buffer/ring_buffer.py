class RingBuffer:
    class RingNode:
        def __init__(self):
            self.value = None
            self.next = None

    def __init__(self, capacity):
        self.capacity = capacity
        
        # create head node
        # only reason to track head node is (IMO incorrect) requirements
        # in the example and tests that the items returned from .get()
        # start with the first 'slot' that was filled instead of starting
        # with the oldest item in the buffer
        self.first_node = RingBuffer.RingNode()
        
        # keep track of capacity while initializing buffer
        capacity = capacity - 1

        # node pointer
        self.current_node = self.first_node

        # create remaining ring
        while capacity > 0:
            self.current_node.next = RingBuffer.RingNode()
            self.current_node = self.current_node.next
            capacity = capacity - 1
        
        # chain ring back to head
        self.current_node.next = self.first_node

        # reset node pointer to head
        # only need to do this because of requirements
        # a real ring buffer wouldn't track a 'starting point'
        # because it is circular
        self.current_node = self.first_node


    def append(self, item):
        # set value
        self.current_node.value = item
        # move forward in chain
        self.current_node = self.current_node.next

    def get(self):
        items = []

        # start at head (due to spec / tests)
        # actual ring node should start at oldest item
        # which would be `self.current_node`
        current_node = self.first_node
        # walk chain, retrieve non-null values
        for i in range(self.capacity):
            if current_node.value is not None:
                items.append(current_node.value)
            current_node = current_node.next

        return items