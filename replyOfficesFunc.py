from dijkstra import *
class Work:
  distanceList = []
  def __init__(self,Data,xMapSize,yMapSize,co,ro):
    self.Data = Data
    self.xMapSize = xMapSize
    self.yMapSize = yMapSize
    self.co = co
    self.ro = ro
  
  def groupCustomers(self):
    ratio = round(self.co/self.ro+0.49)  
    g = Graph(self.xMapSize * self.yMapSize)
    








  def getReplyOfficePlace(self,customerList):
    heatMapList = []
    
    #teile addierte Heatmap durch anzahl der Teilnehmer für durchschnitt
    for i in range(heatMapList):
      heatMapList[i] /= len(customerList)
    
    








