# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23  2017

@author: maque

Note the demo code and well illustrated in the link below:
http://interactivepython.org/runestone/static/pythonds/BasicDS/SimulationHotPotato.html
Also, you can treat the hot_potato problem as Josephus problem, from the link:
https://en.wikipedia.org/wiki/Josephus
"""

from queue import Queue

def hot_potato(name_list, num):
    simu_queue = Queue()
    for name in name_list:
        simu_queue.enqueue(name)
        
    while simu_queue.size() > 1:
        for i in range(num):
            simu_queue.enqueue(simu_queue.dequeue())
            
        simu_queue.dequeue()
        
    return simu_queue.dequeue()


print(hot_potato(list(range(41)), 2))

## the answer is 30, which is the 31th position, which is the Josephus's position