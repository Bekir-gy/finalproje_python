# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 16:12:14 2021

@author: Lenovo
"""
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph() 
E = [('3', '4', 5), ('3', '1', 2), ('3', '2', 3), ('1', '4', 1), ('4', '5', 6), ('2', '6', 4), ('6', '5', 7)]
G.add_weighted_edges_from(E)

pos=nx.spring_layout(G)

nx.draw(G, pos, with_labels=True, font_weight='bold')

edge_weight = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_weight)

plt.show()