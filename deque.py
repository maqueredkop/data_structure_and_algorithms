# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23  2017

@author: maque
Note the demo code is from <Problem solving with algorithms and data structure>
"""

class Deque:
    """
    A deque, also known as a double-ended queue.
    New items can be added at either the front or the rear. Likewise, 
    existing items can be removed from either end.
    """
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
    
    def add_rear(self,item):
        self.items.insert(0,item)
        
    def add_front(self,item):
        self.items.append(item)
        
    def remove_rear(self):
        return self.items.pop(0)
    
    def remove_front(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
d = Deque()

d.is_empty()
d.add_front('duck')
d.add_front('cock')
d.add_rear('goose')
d.add_rear('mouse')
d.size()
d.remove_front()
d.remove_rear()
d.size()


