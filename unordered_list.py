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
        
    