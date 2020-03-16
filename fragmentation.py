# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 19:15:36 2020

@author: 18pw08
"""

def get_mtu(p1,p2):
    
    mtu=[[('A','C'),1500],[('A','D'),3500],[('B','C'),1000],[('C','D'),2000],[('C','F'),1000],
          [('D','E'),1500],[('F','E'),1400]]

    for i in range(len(mtu)):
        if mtu[i][0][0]==p1 and mtu[i][0][1]==p2:
            return mtu[i][1]
        elif  mtu[i][0][0]==p2 and mtu[i][0][1]==p1:
            return mtu[i][1]
    
#routing
client={'c1':'A','c2':'B','c3':'E','c4':'F'}
A={'B':'C','C':'C','D':'D','E':'C','F':'C'}
B={'A':'C','C':'C','D':'C','E':'C','F':'C'}
C={'A':'A','B':'B','D':'D','E':'F','F':'F'}
D={'A':'A','B':'C','C':'C','E':'E','F':'E'}
E={'A':'D','B':'F','C':'F','D':'D','F':'F'}
F={'A':'C','B':'C','C':'C','D':'E','E':'E'}

point={'A':A,'B':B,'C':C,'D':D,'E':E,'F':F}

src=input('Enter the Source Client:')
dest=input('Enter the destination Client:')

s_p=client[src]
d_p=client[dest]

temp=s_p

rout=[]
while temp!=d_p:
    rout.append(temp)
    r=point[temp]
    temp=r[d_p]
rout.append(d_p)

print('The path is :',rout)

packet_size=input('Enter the packet size:')
packet_size=int(packet_size)
header=input('Enter the header size:')
header=int(header)

flag=0
prev_packet_size=packet_size
current=rout[0]
destination=rout[-1]

while current != destination:
    

    prev=current
    flag=flag+1
    current=rout[flag]
    print('\n')
    print('From ',prev,'To ',current)
    
    m=get_mtu(prev,current)
    data_size=m
    data_size=data_size-header
    data_size=(data_size)-(data_size % 8)

    address=0
    i=1
    
    while address<packet_size:
        while address<prev_packet_size*i and address<packet_size:
            print(address//8,end=' ')
            address=address+data_size
        i=i+1
        addres=prev_packet_size*i
    prev_packet_size=data_size