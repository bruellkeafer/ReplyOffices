from dijkstra import *
from setData import *
from classes import *
from array import *
from replyOfficesFunc import *
import copy

"""
>in Map Kosten eintragen X -> weightList

>C/O gruppen für Customer finden
  -C/O berechnen X
  -Gruppen finden mit Dijkstra

>Heatmap generieren
  -Dijkstra

>Heatmaps der C/O Offices addieren

>Office auf kleinsten Wert stellen
"""

out = open("output.txt", "w")
file = open("input.txt", "r")

headline = file.readline().split()

xMapSize = (int)(headline[0])
yMapSize = (int)(headline[1])
co = (int)(headline[2])  #Costumer Offices count
ro = (int)(headline[3])  #Reply Offices count

mapList = []
customerList = []

Datasetter = setData(mapList,customerList)
Datasetter.setmapList(file,xMapSize,yMapSize,co,ro)
work = Work(Datasetter,xMapSize,yMapSize,co,ro)

#g.dijkstra(0); 
#Reihenfolge der TerrainTypen "#~*+X_HT = [0,800,200,150,120,100,70,50]"

costList = copy.deepcopy(mapList)
print(Datasetter.mapList)
print(Datasetter.weightList)
#print("\n\n" + Datasetter.mapList[5][5])
work.groupCustomers();





