#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:50:09 2019

Byzantinum Attack emulator 
"""

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import networkx as nx
import random
import argparse

from matplotlib.offsetbox import  OffsetImage, AnnotationBbox #,TextArea, DrawingArea,
import matplotlib.image as mpimg

pirate = mpimg.imread('pirate.png')
Byzantium = mpimg.imread('Byzantium.png')

parser = argparse.ArgumentParser(description='Number of nodes')
parser.add_argument('-nd', type=int,default=12, help='Number of nodes')
n_nodes = parser.parse_args()
n_nodes = n_nodes.nd
TG=nx.Graph()
for i in range(n_nodes):
    TG.add_node(i+1,image=Byzantium,size=0.05)
edges = []

for i,n in enumerate(list(TG.nodes())):
        j=n_nodes-1
        while j>i:
            edges.append((list(TG.nodes())[i], list(TG.nodes())[j]))
            j-=1
TG.add_edges_from(edges)
TG_sub_nodes = []
POS = nx.spring_layout(TG)
ecTG = "pink"
ec = "firebrick" 
face_c = "sienna"
props = {'boxstyle':'sawtooth', 'facecolor':'wheat', 'alpha':0.5}
comment = "Stable system"
l=1
N=0
n_blick = 2
blick_show = .007
pause = .65
if __name__ == '__main__':
    plt.ion()
    while  l <= len(TG):
        SubTG = TG.subgraph(TG_sub_nodes)

        fig = plt.figure(1,figsize=(10,10))
        plt.xkcd()
        ax = fig.add_subplot(1, 1, 1)
        ax.set_facecolor("sienna")
       
        imageboxB = OffsetImage(Byzantium, zoom=0.15)
        abB = AnnotationBbox(imageboxB, (-0.94, 0.96))
        ax.add_artist(abB)
        
        if len( TG_sub_nodes) == n_nodes - 1: 
            ec = "k"
            ecTG = "seashell"
            comment = "Base ideology totaly changed"
            for i in range(n_blick):
                ax.set_facecolor(face_c) 
                plt.pause(blick_show)
                ax.set_facecolor("silver")
                plt.pause(blick_show)

        elif len( TG_sub_nodes) >= n_nodes*2/3: 
            ec = "darkgrey"
            comment = "Bad boys are gone god"
            ax.set_facecolor(face_c) 

        elif len( TG_sub_nodes) >= n_nodes /3: 
            ec = "darkgrey" 
            comment = "Bad boys won"
            ax.set_facecolor(face_c) 

        elif len( TG_sub_nodes) >= n_nodes /4: 
            ec = "darkgrey" 
            comment = "Bad boys are going stronger"
            ax.set_facecolor(face_c) 

        textstr = "\n".join((r'Nonloyal part is $ %.2f$                  ' % (len( TG_sub_nodes)/n_nodes, ), comment))
        
        
        
        ax.text(0.72, 0.98, textstr, transform=ax.transAxes, fontsize=10,
                    verticalalignment='top', bbox=props)
        
        nx.draw_networkx(TG, pos=POS,  edge_color=ecTG, node_size=1, with_labels=False)
        
        for i in range(n_blick):
            
            nx.draw_networkx(SubTG, pos=POS,  edge_color="red", node_size=1, with_labels=False)
            plt.pause(blick_show)
            nx.draw_networkx(SubTG, pos=POS,  edge_color=ec,  node_size=1, with_labels=False)
            plt.pause(blick_show)
       
        
        plt.gcf().canvas.flush_events()

        label_pos = 0.5 # middle of edge, halfway between nodes
        trans = ax.transData.transform
        trans2 = fig.transFigure.inverted().transform
        imsize = 0.1 # this is the image size
        if N: TG.add_node(N, image=pirate,size=0.05) ####
        for n in TG.nodes():
            (x1,y1) = POS[n]
   
            xx1,yy1 = trans((x1,y1))
            xa1,ya1 = trans2((xx1,yy1))
            imsize = TG.nodes[n]['size']
            img =  TG.nodes[n]['image']
            aa = plt.axes([xa1-imsize/2.0,ya1-imsize/2.0, imsize, imsize ])
            aa.imshow(img)
    
            aa.set_aspect('equal')
            aa.axis('off')
        
        plt.pause(pause)
        set_TG = set(TG)
        set_TG_sub_nodes = set(TG_sub_nodes)
        N = random.sample(set_TG.difference(set_TG_sub_nodes),1)[0]
        TG_sub_nodes.append(N)
        l+=1
    
    imagebox = OffsetImage(pirate, zoom=0.15)
    ab = AnnotationBbox(imagebox, (-0.94, 0.96))
    ax.add_artist(ab)
   
    
    plt.ioff()   
    plt.show()
       