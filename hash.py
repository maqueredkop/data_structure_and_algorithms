# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5  2017

@author: maque

Note that the demo code is from the below link:
http://interactivepython.org/courselib/static/pythonds/SortSearch/Hashing.html
and add some other operations  in the exercises.
"""

class Hash_table:
    
    '''
    put(key,val) Add a new key-value pair to the map. If the key is already in
    the map then replace the old value with the new value.
    
    get(key) Given a key, return the value stored in the map or None otherwise.
    
    del Delete the key-value pair from the map using a statement of the form del map[key].
    
    len() Return the number of key-value pairs stored in the map.
    
    in Return True for a statement of the form key in map, if the given key
    is in the map, False otherwise.
    
    Note that the hash_function implements the simple remainder method. The 
    collision resolution technique is linear probing with a “plus 1” rehash function.
    '''
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
        
    def put(self, key, data):
        hash_value = self.hash_function(key, len(self.slots))
        
        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
            
        elif self.slots[hash_value] == key:
            self.data[hash_value] = data
            
        else:
            next_slot = self.rehash(hash_value, len(self.slots))
            while self.slots[next_slot] != None and self.slots[next_slot] != key:
                next_slot = self.rehash(next_slot, len(self.slots))
                
            if self.slots[next_slot] == None:
                self.slots[next_slot] = key
                self.data[next_slot] = data
            else:
                self.data[next_slot] = data
                
    def hash_function(self, key, size):
        return key % size
    
    def rehash(self, old_hash, size):
        return (old_hash + 1) % size
    
    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))
        
        data = None
        stop = False
        found = False
        position = start_slot
        
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True
                    
        return data
    
    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self, key, data):
        self.put(key, data)
        
    def __delitem__(self, key):
        if key in self.slots:
            position = self.slots.index(key)
            self.slots[position] = None
            self.data[position] = None
            
    #def len(self):
    def __len__(self):
        length = 0
        for key in self.slots:
            if key != None:
                length = length + 1
        return length
    
    def __contains__(self, key):
        return key in self.slots
     
        
test_hash = Hash_table()
test_hash[54] = 'cat'
test_hash[26] = 'dog'
test_hash[93] = 'lion'
test_hash[17] = 'tiger'
test_hash[77] = 'bird'
test_hash[31] = 'cow'
test_hash[44] = 'goat'
test_hash[55] = 'pig'
test_hash[20] = 'chicken'

print(test_hash.slots)
print(test_hash.data)

print(test_hash[20])
print(test_hash[17])

test_hash[20] = 'duck'
print(test_hash[20])

print(test_hash[99])

del test_hash[54]
print(test_hash.slots)
print(test_hash.data)

77 in test_hash
100 in test_hash

print(len(test_hash))
