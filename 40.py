# Detect loop in linked list
def detect_loop(head):
    # A set to store the memory addresses of nodes we've seen
    visited_nodes = set()
    
    current = head
    while current:
        # If the current node is already in our 'seen' list, it's a loop
        if current in visited_nodes:
            return True
            
        # Add the current node to our 'seen' list
        visited_nodes.add(current)
        
        # Move to the next node
        current = current.next
        
    # If we get out of the loop, we hit the end of the list (no cycle)
    return False