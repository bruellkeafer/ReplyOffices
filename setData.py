from classes import *
#import globalVariables
#Global Variables



class setData:
  xMapSize = 0
  yMapSize = 0
  getWeight = {"#":0, "~":800, "*":200, "+":150, "X":120, "_":100, "H":70, "T": 50}
  weightList = []


  def __init__(self,mapList,customerList):
        self.mapList = mapList
        self.customerList = customerList

  def setmapList(self,file,xMapSize,yMapSize,co,ro):
    self.xMapSize = xMapSize
    self.yMapSize = yMapSize
    for i in range(0,co):
      info = file.readline().split()
      self.customerList.append(costumerOffice())
      self.customerList[i].x = (int)(info[0])
      self.customerList[i].y = (int)(info[1])
      self.customerList[i].reward = (int)(info[2])
    #print(str(customerList[i].x)+' '+str(customerList[i].y)+' '+str(customerList[i].reward))
  
    # read Map from input to mapList
    for i in range(self.yMapSize):
      mapColumn = file.readline().split()
      self.mapList = self.mapList + mapColumn

    #Gewichtung der mapList
    for row in range(self.yMapSize):
      self.weightList.append([])
      for column in range(self.xMapSize):
        self.weightList[row].append(self.getWeight[self.mapList[row][column]])
  
