class node:
    def __init__(self,val):
        self.val = val
        self.next = None
        
class linkedList:
    def __init__(self):
        self.head = None
    
    def append(self,val):
        new_node = node(val)
        
        if not self.head:
            self.head = new_node
            return
        
        crr = self.head
        while crr.next:
            crr = crr.next
        crr.next = new_node