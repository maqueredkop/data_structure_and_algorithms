#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 20:38:01 2017

@author: maque
"""

class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
        
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_data(self,new_data):
        self.data = new_data
        
    def set_next(self, new_next):
        self.next = new_next
        
temp = Node(10)
temp.get_data()
temp.get_next()


class Unordered_list:
    
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head == None
    
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
 
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
            
        return count
    
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        
        return found
    
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
                
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
            
            
my_unorder_list = Unordered_list()
my_unorder_list.is_empty()
my_unorder_list.size()
my_unorder_list.add(21)
my_unorder_list.add(56)
my_unorder_list.add(78)
my_unorder_list.is_empty()
my_unorder_list.size()
my_unorder_list.search(56)
my_unorder_list.search(100)
my_unorder_list.remove(21)
my_unorder_list.size()
    
